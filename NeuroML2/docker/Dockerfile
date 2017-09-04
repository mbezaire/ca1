#
# A Docker image for running the CA1 network model
#
# This image extends the "opensourcebrain/simulation" image 
#

FROM opensourcebrain/simulation:osb-v0.2
MAINTAINER p.gleeson@gmail.com

USER root

RUN apt-get update 


# Clone CA1 repository


RUN git clone https://github.com/mbezaire/ca1.git


RUN echo "Built!"



