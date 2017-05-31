classdef SimRun < handle
   properties % (Hidden) (SetAccess = private)
       % displayed in list view and form view
       % we may need to move the initializations to the constructor fcn
       % (but keep the list of properties in here, obviously)
        RunName = 'none' % Name of simulation run
        UID = '0' % Unique ID for this simulation run
        ModelVerComment = '' % Model code Mercurial version number and comment
        ExecutionDate = '' % Date simulation was executed
        Stimulation = 'spontaneous' % Filename of the stimulation protocol used to stimulate the network
        NumSpikes = 0 % Total number of spikes from all cells during the simulation
        Connectivity = 'try_all_randfaststim' % Filename of the connection protocol used to connect the cells of the network
        NumConnections = 0 % Total number of connections in the network
        Scale = 1000 % Network scale (1:Scale)
        NumCellTypes = 0 % Total number of cell types in the network
        SimDuration = 300 % Duration of time simulated, in milliseconds
        RunTime = 0 % Total time taken by processor 0 in seconds
        Machine = 'localhost' % Computer the code was run on
        NumProcessors = 1 % Number of processors used to perform a parallel job
        RandomSeeds = 0 % Method used to assign seeds to random processors
        NEURONVersion = '' % Mercurial version of the NEURON code used to run the simulation
        ModelDirectory = '' % Directory on the local machine of the program code and results folders
        RemoteDirectory = '' % Directory of the program code and results folders on the machine the simulation was executed
        ExecutedBy = '' % Username of the person logged into the computer where the simulation was executed
        Positioning = '' % Algorithm used to position the cells
        PrintVoltage = 1 % Flag for recording and printing intracellular voltage traces for select cells
        PrintTerminal = 1 % Level of printouts to screen (affects run time) 0: minimal, 1: some, 2: max printouts
        PrintConnDetails = 0 % Flag for printing the detailed connection matrix
        PrintCellPositions = 1 % Flag for printing the cell positions
        PrintConnSummary = 1 % Flag for printing the summary connection matrix
        TransverseLength = 1000 % Length of the network subfield in the transverse direction in microns
        LongitudinalLength = 4000 % Length of the network subfield in the longitudinal direction in microns
        LayerHeights = '4;100;50;200;100;' % Vector of heights of each network subfield layer in microns (from basal to molecular layer)
        SpatialResolution = 100 % Spatial discretization method or resolution
        ConnData = 100 % Number of the connection dataset to use
        SynData = 100 % Number of the synapse kinetics dataset that was used to prepare the cell definition files
        NumData = 100 % Number of the cells dataset to use
        RunComments = '' % Comments about the run, entered into the RunOrganizer
        NumCellsRecorded = 1 % Number of cells whose voltages were traced throughout the simulation
        NumCells = 1 % Number of real cells in the network
        ModelVersion = '' % Full Mercurial Version of the NEURON code used to run the simulation
        TemporalResolution = 0.1 % Temporal resolution of the simulation (in ms)
        JobScript = '' % File name of job script used to submit run to queueing software
        ModelName = '' % Main model code file that was run (often named for the subfield of the network
        Errors = '' % Description of an error that occurred during the run, breaking the simulation (hand entered)
        Groups = '' % User-defined groups that the run is a member of
        NumTraces = 100 % The maximum number of cells to record intracellularly, for each cell type
        FracTraces = 50 % The percent of cells to record intracellularly, for each cell type
        JobNumber = 0 % Job number assigned by supercomputer
        StepBy = 100 % Number of ms to run at a time
        JobHours = 4 % Number of hours to let the run go for
        EstWriteTime = 660 % Number of seconds to save for the run to write out its results
        TopProc = '' % NEURON process name in the top command
        DegreeStim = 10 % Degree of stimulation; meaning depends on Stimulation type
        CatFlag = 1 % Whether to concatenate and remove trace connection files
        RandomSeedsConn = 0 % Starting highIndex used by connectivity streams
        RandomSeedsStim = 0 % Starting highIndex used by stimulation streams
        AxConVel = 0 % Axonal conduction delay in um/ms, usually 250-500
        myConDelay = 1.2 % Axonal conduction delay
        ComputeLFP = 0 % Positive value indicates that approximate pyramidal cell LFP should be computed
        NumTracesPyr = 3000 % The maximum number of pyramidal cells to record intracellularly
        MaxEDist = 1000 % The maximum distance in microns away from an electrode point that LFP contributions from cells should be included
        lfp_dt = .5 % The time step for recording the LFP trace
        ElectrodePoint = '200;100;120' % X,Y,Z coordinates of LFP recording electrode, in microns, separated by semicolon
        ComputeNpoleLFP = 1 % Compute the LFP using all or a fraction of compartments from nearby pyramidal cells
        ComputeDipoleLFP = 0 % Compute the LFP using two compartments (dipole) of nearby pyramidal cells
        LFPCellTypes = 'pyramidalcell' % semicolon separated list of cell types to record LFP from (give full name of celltype) -- ONLY WORKS FOR NPOLE!
        RandomVrest = 0.0 % Standard deviation away from Vrest for RMP of each cell
        RandomVinit = 0 % Positive value indicates that initial voltages should be randomized
        PhasicData = 100 %  Which phasic dataset to use for oscillation/phasic stimulation
        PercentCellDeath = 0 %  Percent of cells that are killed (removed), for cell types flagged for cell death
        RandomSynWgt = 0 % >0 indicates that synapse weights should vary with the specified weight as the mean. 1: a normal distribution, 2: a lognormal distribution, 3: a uniform distribution
        synVar = 0.03 %  Fraction of the mean synapse weight that should be set as the standard deviation in the normal distribution of synapse weights for randomized synapse weights
end
   methods
      function BA = SimRun(RunName,ResultsDirectory,UID)
          global RunArray
         if nargin < 2
            error('SimRun:InvalidInitialization',...
               'You must provide a Run Name and directory to uniquely identify this simulation record')
         end
         BA.RunName  = RunName;
         BA.ModelDirectory = ResultsDirectory;
         BA.UID = UID;
         if exist('RunArray')==0 || strcmp(class(RunArray),'double') % double happens when the variable didn't exist and was then declared global
            RunArray=BA;
         else
            RunArray(length(RunArray)+1)=BA;
            while sum(strcmp({RunArray(:).RunName},BA.RunName))>1
                newname=inputdlg('Run Name already used. Enter a new one:');
                BA.RunName=newname{1};
            end
         end
      end % SimRun
      function set.UID(BA,val)
         if (isempty(BA.UID) || strcmp(BA.UID,'0'))
            BA.UID = val;
         else
             msgbox({'Cannot change UID. UID already set to:',BA.UID});
         end
      end
      function set.RunName(BA,val)
         if isempty(BA.ExecutionDate)
            BA.RunName = val;
         else
             msgbox('Cannot change Run Name after run has been executed');
         end
      end
      function loadexecdata(BA)
          sl='/';
          tmpdir = BA.ModelDirectory; % right now it is set to the local directory, but during the while statement it will be set to the remote directory
         if exist([BA.ModelDirectory sl 'results' sl BA.RunName sl 'runreceipt.txt']) > 0
            sl='/';
            fid = fopen([BA.ModelDirectory sl 'results' sl BA.RunName sl 'runreceipt.txt'],'r');
            while ~feof(fid)
                setval=fgetl(fid);
                myprop=regexp(setval,'([\w]+)','tokens','once');
                if sum(strcmp(myprop,properties(BA))) && strcmp(myprop,'RunName')==0 && (strcmp(myprop,'UID')==0 || isempty(BA.UID))
                    eval(['BA.' setval]);
                end
            end
            fclose(fid);
         end
         BA.RemoteDirectory = BA.ModelDirectory;
         BA.ModelDirectory = tmpdir;
         if exist([BA.ModelDirectory sl 'results' sl BA.RunName sl 'sumnumout.txt']) > 0
            fid = fopen([BA.ModelDirectory sl 'results' sl BA.RunName sl 'sumnumout.txt'],'r');
            while ~feof(fid)
                setval=fgetl(fid);
                myprop=regexp(setval,'([\w]+)','tokens','once');
                if sum(strcmp(myprop,properties(BA)))
                    eval(['BA.' setval]);
                end
            end
            fclose(fid);
         end
      end % loadexecdata
   end % methods
end % classdef
