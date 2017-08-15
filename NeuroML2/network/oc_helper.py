#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
The function below modifies an oc.core function, using the same oc.build function, and allows to add correlated convergent input to populations
TODO: make a pull request to OpenCortex?
Authors: András Ecker, Padraig Gleeson, last update: 08.2017
"""

import neuroml
import opencortex.build as oc_build

def add_targeted_corr_input(nml_doc,
                            net,
                            prefix,
                            presynaptic_population,
                            postsynaptic_population,
                            synapse_list,
                            number_conns_per_cell,
                            post_segment_group,
                            delays_dict=None,
                            weights_dict=None):
    """
    This function is modified from oc.add_targeted_projection to allow a population of 'artificial cells' (eg.spikeGeneratorPoisson) to make convergent projections to population of 'real cells' (having morphology...) in order to make the input correlated (instead of using uncorrelated oc.add_targeted_inputs_to_population)
    (see original source here: https://github.com/OpenSourceBrain/OpenCortex/blob/master/opencortex/core/__init__.py#L394)
    """
    
    projections = []
    
    post_cell = oc_build.cell_ids_vs_nml_docs[postsynaptic_population.component].get_by_id(postsynaptic_population.component)

    post_segs = oc_build.extract_seg_ids(post_cell, [post_segment_group], "segGroups")
    post_seg_target_dict = oc_build.make_target_dict(post_cell, post_segs)

    for synapse in synapse_list:
        proj_id = "%s_%s_%s"%(prefix, presynaptic_population.id, postsynaptic_population.id) if len(synapse_list) == 1 else \
"%s_%s_%s_%s"%(prefix, presynaptic_population.id, postsynaptic_population.id, synapse)
        # should be opencortex.print_comment_v()...
        print("Adding projection: %s: %s -> %s (%s)"%(proj_id, presynaptic_population.component, post_cell.id, post_segs))
        
        proj = neuroml.Projection(id=proj_id, 
                                  presynaptic_population=presynaptic_population.id, 
                                  postsynaptic_population=postsynaptic_population.id, 
                                  synapse=synapse)
        projections.append(proj)

    subset_dict = {}
    subset_dict[post_segment_group] = number_conns_per_cell

    oc_build.add_targeted_projection_by_dicts(net,
                                              projections,
                                              presynaptic_population,
                                              postsynaptic_population,
                                              targeting_mode="convergent",  # only possible mode: convergent 
                                              synapse_list=synapse_list,
                                              pre_seg_target_dict=None,  # will leave preSegmentId and preFractionAlong in the generated file (which is the way how 'artificial cells' connect to 'real cells')
                                              post_seg_target_dict=post_seg_target_dict,
                                              subset_dict=subset_dict,
                                              delays_dict=delays_dict,
                                              weights_dict=weights_dict)

    return projections 



