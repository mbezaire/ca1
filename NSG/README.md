## Interacting with Neuroscience Gateway Portal

**The folder contains python and bash script to send jobs to supercomputers through [NSG](https://www.nsgportal.org/).**

In order to prepare necessary files from the original NEURON version of the model run:

    python zip_nrn_forNSG.py  # zips necessary files in NSG preferred way

Afterwars you can register an account on https://www.nsgportal.org/gest/reg.php and access the web interface at https://nsgdev.sdsc.edu:8443/portal2/login!input.action
You can upload your `.zip` file and run tasks through their interface! Alternatively you can use the REST API as described below!


#### Sign up to the NSG REST server

1. Go to https://nsgr.sdsc.edu:8443/restusers/login.action and register for a new account
2. Log in to the service
3. Go to Developer -> Application Management
4. Click Create New Application
5. Create the application, describing what you'll be using the service for. **Please take the time to add relevant info here. Having access to this information will help the developers justify the resource and keep it free for the community!**
6. Make sure to set Authentication Type to DIRECT.
7. Make a note of the Application ID
8. Copy the [nsgrest_example.conf](https://github.com/mbezaire/ca1/blob/development/NSG/nsgrest_example.conf) file to **nsgrest.conf** and move it to your home folder
9. Update the details there with the information you entered on the NSG REST server:

    ```
    URL=https://nsgr.sdsc.edu:8443/cipresrest/v1
    USERNAME=uuuuuu
    PASSWORD=xxxxxx
    DIRECT_APPID=Direct111111111111
   ```
   
> `DIRECT_APPID` should be set to your Application ID


#### Access NSG-R using shell scripts

1. Test listing/submitting of jobs with the original NEURON version:

    ```
    ./list_jobs.sh                # none yet...
    ./submit_nrn_toNSG.sh Test 1  # submit NEURON job (ID=Test, number of nodes=1)
    ./list_jobs.sh                # should be listed
    ./status_job.sh JOBIDXXXX     # Replace job ID with that listed above
    ```
    
2. Get results after simulation is finished (and notification was sent by e-mail):

    ```
    ./list_results.sh JOBIDXXXX           # Replace job ID with that listed above (or found in the e-mail)
    # look for output.tar.gz (should be the last one) and <outputDocumentId>
    ./download_results.sh JOBIDXXXX DIDx  # Replace job ID and doc ID with that found above
    ```
    
3. Send NetPyNE jobs to NSG-R, based on the NeuroML2 version (Note: this is not possible through the web interface yet!):

    ```
    python zip_nml_forNSG.py      # zips necessary files in NSG preferred way
    ./submit_nml_toNSG.sh 100000 Test 1 0.5  # submit NetPyNE job (scale=100000, ID=Test, nNodes=1, runTime=0.5)
    # repeat the same as above to get results
    ```
    
see more about `curl` functions used to interact with the REST API [here](https://www.nsgportal.org/guide.html).


> This work is based [OSB's NSG showcase](https://github.com/OpenSourceBrain/NSGPortalShowcase/tree/master/NSG-R), which is on the REST API from [CIPRES - Cyberinfrastructure for Phylogenetic Research](http://www.phylo.org/index.php/news/detail/announcing-cipres-restful-services-a-new-way-to-use-cipres).




