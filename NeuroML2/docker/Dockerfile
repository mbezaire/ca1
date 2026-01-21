#
# A Docker image for running the CA1 network model
#
# This image extends the "opensourcebrain/simulation" image, at a specific tagged version
#

FROM opensourcebrain/simulation:osb-v0.7.1
MAINTAINER p.gleeson@gmail.com

USER root

RUN apt-get update 


# Clone CA1 repository


RUN git clone https://github.com/mbezaire/ca1.git
RUN cd ca1; git checkout development; cd -

RUN cd ca1/NeuroML2 && nrnivmodl .. && cd -


RUN echo "Built!"



