NEURON {
  SUFFIX nothing
}

: gmin - the starting gid for this type of cell
FUNCTION get_x_pos(gid, gmin, BinNumX, BinNumYZ, binSizeX) {
	LOCAL CellNum, tmp
	CellNum=gid - gmin+1
	tmp = floor((CellNum-1)/BinNumYZ)
	get_x_pos =  fmod(tmp,BinNumX)*binSizeX+binSizeX/2.0
	:printf("---get_x_pos=%f\n", get_x_pos)
}

FUNCTION get_y_pos(gid, gmin, BinNumY, BinNumZ, binSizeY) {
	LOCAL CellNum, tmp, pos
	CellNum=gid - gmin+1
	tmp = floor((CellNum-1)/BinNumZ)
	get_y_pos =  fmod(tmp,BinNumY)*binSizeY+binSizeY/2.0
}

FUNCTION get_z_pos(gid, gmin, BinNumZ, binSizeZ, ZHeight) {
	LOCAL CellNum, pos
	CellNum=gid - gmin+1
	get_z_pos = fmod((CellNum-1),BinNumZ)*binSizeZ+binSizeZ/2+ZHeight
}


COMMENT
VERBATIM
static double get_x_pos (int gid, int gmin, int BinNumX, int BinNumYZ, int binSizeX) {
	double pos;
	int CellNum, tmp;
	CellNum=gid - gmin+1;
	tmp = floor((CellNum-1)/BinNumYZ);
	pos =  (tmp%BinNumX)*binSizeX+binSizeX/2.0;
	return pos;
}
ENDVERBATIM

VERBATIM
static double get_y_pos (int gid, int gmin, int BinNumY, int BinNumZ, int binSizeY) {
	double pos;
	int CellNum, tmp;
	CellNum=gid - gmin+1;
	tmp = floor((CellNum-1)/BinNumZ);
	pos =  (tmp%BinNumY)*binSizeY+binSizeY/2.0;
	return pos;
}
ENDVERBATIM

VERBATIM
static double get_z_pos (int gid, int gmin, int BinNumZ, int binSizeZ, int ZHeight) {
	double pos;
	int CellNum;
	CellNum=gid - gmin+1;
	pos = ((CellNum-1)%BinNumZ)*binSizeZ+binSizeZ/2+ZHeight;
	return pos;
}
ENDVERBATIM
ENDCOMMENT