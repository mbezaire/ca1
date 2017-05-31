COMMENT
This fastconn mechanism written by marianne.case@uci.edu on April 19, 2011.
It decreases the time taken to decide which connections to make between
cell by an order of magnitude, compared to Rob & Viji's code (even the
version that I parallelized). How it works, in context with hoc:

for each cell type (as postsynaptic cell type) - hoc
> for each cell type (as presynaptic cell type) - hoc
> > make a vector of gids of all cells owned by this processor
	of the postsynaptic type - hoc
> > send vector, presynaptic cell type axonal distribution,
	number of connections desired to NMODL - hoc
> > for each postsynaptic cell of postsynaptic cell type
	owned by this processor - NMODL
> > > calculate the distance between every presynaptic cell
	  of presynaptic cell type and this postsynaptic cell - NMODL
> > > choose the desired number of connections at various distances - NMODL
	  (as defined by the presynaptic axonal distribution
	  and total # of desired connections) - NMODL
> > > randomly pick the specific connections, up to the desired
	  and/or available number for each distance - NMODL
> > > for each desired connection, add the gid
	  of the presynaptic cell to a vector - NMODL
> > return the filled vector to hoc - NMODL
> > make all the connections listed in the vector - hoc

The way to call this from hoc:
- first, install the vector method with this argument:
	install_fastconn()
	
- then, create a vector with the parameters for the connections
	(parameters described below)
- then, create a vector with the gids of the post synaptic cells
- and finally, create an empty placeholder vector with 3x the elements
	as the number of connections desired
- finally, populate the placeholder vector with the connection
	information using the following command:
conns2make.fastconn(params, postcellgids)

params vector has 26 elements:
0 - start gid of the presynaptic cell type
1 - end gid of the presynaptic cell type (assume continuous range)
2 - total number of connections desired from this presynaptic cell type
	to this postsynaptic cell type
3 - total number of cells of the postsynaptic type
4 - number of cells of postsynaptic type with gids owned by this host
5 - total distance over which distance distribution applies (um)
6 - resolution of the fit to the distribution, in # steps to take
7 - distribution equation coefficient a (for this presynaptic cell type)
8 - distribution equation coefficient b (for this presynaptic cell type)
9 - distribution equation coefficient c (for this presynaptic cell type)
10 - number of position bins along the X axis for presynaptic cell type
11 - number of position bins along the Y axis for presynaptic cell type
12 - number of position bins along the Z axis for presynaptic cell type
13 - length (um) of bins along the X axis for presynaptic cell type
14 - length (um) of bins along the Y axis for presynaptic cell type
15 - length (um) of bins along the Z axis for presynaptic cell type
16 - height in the Z direction, of the layer in which the
	 presynaptic cell type exists
17 - number of position bins along the X axis for postsynaptic cell type
18 - number of position bins along the Y axis for postsynaptic cell type
19 - number of position bins along the Z axis for postsynaptic cell type
20 - length (um) of bins along the X axis for presynaptic cell type
21 - length (um) of bins along the Y axis for presynaptic cell type
22 - length (um) of bins along the Z axis for presynaptic cell type
23 - height in the Z direction, of the layer in which the
	 postsynaptic cell type exists
24 - start gid of the postsynaptic cell type
25 - high index at which to start the random number stream (for each gid)
	 should be set such that there are no overlaps per each gid, so err
	 on the side of caution when setting the next high index.
ENDCOMMENT

VERBATIM
# include <stdlib.h>
# include <stdio.h>
# include <math.h>
ENDVERBATIM

NEURON {
	SUFFIX nothing
}

VERBATIM
extern double* vector_vec();
extern int vector_capacity();
extern void* vector_arg();
extern double get_x_pos(double gid, double gmin, double BinNumX, double BinNumYZ, double binSizeX);
extern double get_y_pos(double gid, double gmin, double BinNumY, double BinNumZ, double binSizeY);
extern double get_z_pos(double gid, double gmin, double BinNumZ, double binSizeZ, double ZHeight);
//void srand(unsigned seed);
ENDVERBATIM

VERBATIM

static  double fastconn (void* vv) {
  int finalconn, ny, nz, nhigh, num_pre, num_post, gmin, gmax, steps, myflaggy, myi, postgmin, stepover;
  double *x, *y, *z, *high, a, b, c, nconv, ncell, axonal_extent;

	/* Get hoc vectors into c arrays */
	finalconn = vector_instance_px(vv, &x); // x is an array corresponding
											// to the placeholder vector
											// of connections to make

	ny = vector_arg_px(1, &y); // y is an array of parameters
	nz = vector_arg_px(2, &z); // z is an array of the postsynaptic gids
	nhigh = vector_arg_px(3, &high); // high is an array of the starting high indices to use
	
	/* Load the parameters from the param array */
	gmin = y[0];	// presynaptic start gid
	gmax = y[1];	// presynaptic end gid
	num_pre = gmax - gmin + 1;	// number of presynaptic cells
	
	nconv = y[2];	// total number of desired connections
	ncell = y[3];	// total number of postsynaptic cells
	num_post = y[4];	// number of postsynaptic cells owned by this host
	axonal_extent = y[5];	// total distance over which distribution fits
	steps = y[6];	// resolution of the distribution fit (in steps)
	a = y[7];		// distribution fit coefficient a
	b = y[8];		// distribution fit coefficient b
	c = y[9];		// distribution fit coefficient c
	postgmin = y[24];	// postsynaptic start gid
	stepover = y[26];	// postsynaptic start gid

	myi=2+num_post;	// myi will give the next index into finalconn
			// 0 is reserved for # conns to make
			// 1 is reserved for # cells (each having an entry for their last high index used by nrnRan4int)

	/* Get positions of the presynaptic and postsynaptic cells*/

	// (1) a single NxM malloc: really this is a large 1-dim array of int values
	//     onto which we will map 2D accesses 
	// 

	// declaration and allocation:

	double *prepos;    // the type is a pointer to a double (the bucket type)
	prepos = (double *)malloc(sizeof(double)*num_pre*3);

	double *postpos;    // the type is a pointer to a double (the bucket type)
	postpos = (double *)malloc(sizeof(double)*num_post*3);

	// in memory: 
	//                   row 0       row 1     row 2 ...
	// 2d_array -----> [ 0, 0, ... , 0, 0, ... 0, 0, ... ] 

	// access using [] notation: 
	//    cannot use [i][j] syntax because the compiler has no idea where the 
	//    next row starts within this chunk of heap space, so must use single 
	//    index value that is calculated using row and column index values and 
	//    the column dimension

	int cell;

	for (cell=0; cell<num_pre; cell++) {
		prepos[cell*3 + 0] = get_x_pos(cell+gmin, gmin, y[10], y[11]*y[12], y[13]);
		prepos[cell*3 + 1] = get_y_pos(cell+gmin, gmin, y[11], y[12], y[14]);
		prepos[cell*3 + 2] = get_z_pos(cell+gmin, gmin, y[12], y[15], y[16]);
	}

	for (cell=0; cell<num_post; cell++) {
		postpos[cell*3 + 0] = get_x_pos(z[cell], postgmin, y[17], y[18]*y[19], y[20]);
		postpos[cell*3 + 1] = get_y_pos(z[cell], postgmin, y[18], y[19], y[21]);
		postpos[cell*3 + 2] = get_z_pos(z[cell], postgmin, y[19], y[22], y[23]);
	}

	/* calculate the distribution of desired connections*/   
	double current_distance [steps], connection_distribution [steps], distribution_denominator, conndist;
	int step, feasible_conns_this_step [steps], desired_conns_this_step [steps];

	distribution_denominator = 0.0;
	int max_fraction_step; max_fraction_step=0;
	for (step=0; step<steps; step++) {
		current_distance[step] = axonal_extent*1.0*(step+1)/(steps); /* current_distance[step] = distance step (in terms of max distance)*/
		//connection_distribution[step] = (1.0/a)*exp(-((current_distance[step]-b)*1.0/c)*((current_distance[step]-b)*1.0/c))*axonal_extent;
		connection_distribution[step] = exp(-a*((current_distance[step]-b)*1.0/c)*((current_distance[step]-b)*1.0/c));
		if (connection_distribution[step]>connection_distribution[max_fraction_step]) {
			max_fraction_step=step;
		}
		distribution_denominator = distribution_denominator + connection_distribution[step];
	}

	if (connection_distribution[max_fraction_step]/distribution_denominator*nconv < 0.5) { //distribution_denominator) { // nconv = nconn*1.0/ncell
		for (step=0; step<steps; step++) {
			desired_conns_this_step[step] = round((2.0*connection_distribution[step]/distribution_denominator)*(nconv));// the number of desired
															// connections for each
															// distance bin step, per cell
		}
	} else {
		for (step=0; step<steps; step++) {
			desired_conns_this_step[step] = round((connection_distribution[step]/distribution_denominator)*(nconv));// the number of desired
															// connections for each
															// distance bin step, per cell
		}
	}

	/* for each postsynaptic cell, find the possible connections and
	 * make the desired number of connections where possible */   
	int m, n, i, q, goupto, rem, extra, szr, szp [steps];
	double distance_between;
	u_int32_t idx1, idx2, maxidx1; // high and low index (seeds) for MCell_Ran4
	maxidx1 = y[25];

	for (n=0; n<num_post; n++) { // for each post cell
		int myx = (int)z[n]; // get the gid of the current postsynaptic cell in int form
		idx1 = high[n];	// reset the high index for the next postsynaptic
						// cell. It should be set to a value that is 
						// certainly higher than what would have been
						// used during previous calls for this low index/gid
						// We accomplish that by setting it equal to the
						// sum of all previous numconns/ncell (for this
						// post cell type, with the previous pre cell types)?
		idx2 = myx;		// set the low index equal to the gid


		double *sortedpos;    // the type is a pointer to a double (the bucket type)
		sortedpos = (double *)malloc(sizeof(double)*num_pre*steps);
		
		//double sortedpos [num_pre][steps];
		for (step=0; step< steps; step++) {
			szp [step]=0; 	// initialize the szp array to 0
							// (it holds a number per bin, telling which
							// index of the array you are on for that bin)
							// when filling the array with available
							// connections for each bin
			feasible_conns_this_step[step] = desired_conns_this_step[step];		
		}
		
		double dist;
		for(m=0; m<num_pre; m++) { // for each pre cell
			// calculate the distance between the pre and post cells
			distance_between = sqrt((1.0*prepos[m*3 +0] - postpos[n*3 +0])*(prepos[m*3 +0] - postpos[n*3 +0])+(prepos[m*3 +1] - postpos[n*3 +1])*(prepos[m*3 +1] - postpos[n*3 +1])+(prepos[m*3 +2] - postpos[n*3 +2])*(prepos[m*3 +2] - postpos[n*3 +2]));
			for (step=0; step< steps; step++) {
				/*if (ncell==2 && num_pre==3) {
					printf("distance=%f step=%d stepmax=%f gmin=%d postg=%d\n", distance_between, step, current_distance[step], gmin, postgmin);
				}*/

				if (distance_between<= current_distance[step]) // if the distance is less than the max distance for that step
				{
					sortedpos[szp [step]*steps + step] = m;
					//sortedpos [szp [step]] [step] = m;	// add this pre cell to this particular bin's column (the next row, which szp keeps track of)
					szp [step]++;
					break;
				}
			}
		}

		/*if (ncell==2 && num_pre==3) {
			for (step=0; step< steps; step++) {
				printf("step: %d  szp: %d\n", step, szp [step]);
			}
		}*/

		// now, this particular post cell has an array (sortedpos) where each
		// column contains a bunch of pre-cell gids whose distances fit within
		// that column's "step" or "distance bin"
		// There is also a feasible_conns_this_step array that gives the ideal # of connections
		// for each step
			
		rem=0;extra=0;
		for (step=0; step<steps; step++) {	// for each step except the last one
			szr = szp [step]; // Get the number of available connections for this step
			if (feasible_conns_this_step[step] + rem> szr) { //If more are wanted than are available,
				rem=feasible_conns_this_step[step]+rem-szr;
				// check the previous level (closer level) for extras
				if (step>0) {
					for(i=1; i<=step; i++) {
						if (szp [step-i] > feasible_conns_this_step[step-i]) {
							if (szp [step-i] - feasible_conns_this_step[step-i]>rem) {
								extra = rem;
							} else {
								extra = szp [step-i] - feasible_conns_this_step[step-i];
							}
							feasible_conns_this_step[step-i] = feasible_conns_this_step[step-i] + extra;
							feasible_conns_this_step[step] = feasible_conns_this_step[step] - extra;
							rem = rem - extra;				
						}
					}
				}
				if (rem>0 && step<steps-1) { // if that still doesn't satisfy all the remainder
					for(i=step+1; i<steps; i++) {				
						if (szp [i] > feasible_conns_this_step[i]) {
							if (szp [i] - feasible_conns_this_step[i]>rem) {
								extra = rem;
							} else {
								extra = szp [i] - feasible_conns_this_step[i];
							}
							feasible_conns_this_step[i] = feasible_conns_this_step[i] + extra;
							feasible_conns_this_step[step] = feasible_conns_this_step[step] - extra;
							rem = rem - extra;
						}
					}
				}
			}
		}

		/*if (ncell==2 && num_pre==3) {
			for (step=0; step< steps; step++) {
				printf("step: %d  szp: %d  feasible_conns_this_step: %d\n", step, szp [step], feasible_conns_this_step[step]);
			}
		}*/
	
		rem=0;
		for (step=0; step<steps; step++) {	// for each step
			if (feasible_conns_this_step[step]>0) { // if this particular step wants any connections
				/* Find all the possible connections for each distance level  */
				
				/*if (ncell==2 && num_pre==3) {
					printf("precells=%d postcells=%d step=%d szr=%d\n", num_pre, ncell, step, szr);
				}*/
				
				szr = szp [step]; // Get the number of available connections for this step
				int r[szr]; // Define an array the length of the number of available connections
				for (i=0; i< szr; i++) { 
					r[i] =  sortedpos[i*steps + step];
					//r[i] =  sortedpos [i] [step]; // Fill the array with the available connections (in terms of the pre cell)
				}

				/* this random routine allows a pre-cell to make multiple connections on the post cell*/
				int tmp;
				u_int32_t randi;
				for (i=0; i<szr-1; i++) {
					randi =  nrnRan4int(&idx1, idx2) % (u_int32_t)szr; // limit to the range of indices in the r array
					tmp = r [i];	// randomly reorganize the pre cells in the r array
					r[i] = r[randi];
					r[randi] = tmp;
				}

				if (feasible_conns_this_step[step]>szr) { 	// if the number of desired connections (ones wanted in this step, plus unmade ones from previous steps)
										// is more than the available amount, set the remainder to the excess ones that can't be made in this step
					goupto=szr;			// and set the number to make (based on the desired and available amts)
				} else {
					goupto=feasible_conns_this_step[step];	// set the number to make (based on the desired and available amts)
				}

				for (q=0; q<goupto; q++) { 	// for each one to make, r[q] gives the precell index in the pre_pos array (this program assumes
											// the gid range is continuous from gmin to gmax arguments to this mechanism.
											// n is the post-cell here. 
					x [myi] = (r[q]+gmin)*1.0;				// presynaptic gid	
					if (num_post>1) {
						x [myi+1*stepover] = (z[n])*1.0;	// postsynaptic gid
						//x [myi+2*stepover] = (step+1)*1.0;	// distance step
					}
					myi++;
				}
			} 
		}
		x [2+n] = idx1 + 1;
		//if (idx1>maxidx1) { maxidx1=idx1;}
		free(sortedpos);
	}
	x [0] = myi-2-num_post;	// fill the first element of the array (vector)
					// with the total number of connections to make,
					// which may be less than the desired number (and
					// hence the size of the array)
	x [1] = num_post; // (double)maxidx1;
	
	free(prepos);
	free(postpos);
	return finalconn;
}
ENDVERBATIM

: This PROCEDURE install_fastconn() should be called from hoc
: to make the fastconn procedure available there

PROCEDURE install_fastconn () {
	VERBATIM
	install_vector_method("fastconn", fastconn);
	ENDVERBATIM
}
