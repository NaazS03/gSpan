import copy
def filter_nonmaximal_subgraphs(frequent_subgraphs_original, projected_frequent_subgraphs_original):
    frequent_subgraphs = copy.deepcopy(frequent_subgraphs_original)
    projected_frequent_subgraphs = copy.deepcopy(projected_frequent_subgraphs_original)
    #Get the size of the min and max subgraphs
    (min_subgraph_size, max_subgraph_size) = find_min_and_max_size_subgraph(frequent_subgraphs)

    #subgraphs_and_projections[0] are the frequent subgraphs
    #subgraphs_and_projections[1] are the projected versions of the frequent subgraphs
    subgraphs_and_projections = connect_subgraphs_with_projections(frequent_subgraphs,projected_frequent_subgraphs)

    #Split the subgraphs into buckets based on their size minus the min subgraph size
    frequent_subgraphs_with_projections_split_by_size = split_subgraphs_with_projections_by_size(subgraphs_and_projections, min_subgraph_size, max_subgraph_size)

    filter_subgraph_buckets(frequent_subgraphs_with_projections_split_by_size)

    print_subgraph_buckets(frequent_subgraphs_with_projections_split_by_size)

def find_min_and_max_size_subgraph(subgraphs):
    min_subgraph_size = subgraphs[0].get_num_vertices()
    max_subgraph_size = subgraphs[0].get_num_vertices()

    for subgraph in subgraphs:
        subgraph_size = subgraph.get_num_vertices()

        if subgraph_size > max_subgraph_size:
            max_subgraph_size = subgraph_size

        elif subgraph_size < min_subgraph_size:
            min_subgraph_size = subgraph_size

    return (min_subgraph_size, max_subgraph_size)

def connect_subgraphs_with_projections(frequent_subgraphs, projected_frequent_subgraphs):
    subgraphs_and_projections = []

    for index in range(0,len(frequent_subgraphs)):
        subgraphs_and_projections.append((frequent_subgraphs[index],projected_frequent_subgraphs[index]))

    return subgraphs_and_projections

def split_subgraphs_with_projections_by_size(subgraphs_and_projections, min_subgraph_size, max_subgraph_size):
    subgraph_size_range = max_subgraph_size - min_subgraph_size
    num_subgraph_size_buckets = subgraph_size_range + 1
    frequent_subgraphs_with_projections_split_by_size = [[] for i in range(0, num_subgraph_size_buckets)]

    for subgraph_and_projection in subgraphs_and_projections:
        subgraph_size = subgraph_and_projection[0].get_num_vertices()
        subgraph_bucket = subgraph_size-min_subgraph_size
        frequent_subgraphs_with_projections_split_by_size[subgraph_bucket].append(subgraph_and_projection)

    return frequent_subgraphs_with_projections_split_by_size

def filter_subgraph_buckets(frequent_subgraphs_with_projections_split_by_size):
    # For each bucket of subgraphs
    for index in range(0, len(frequent_subgraphs_with_projections_split_by_size)):
        # Grab a specific bucket of subgraphs to start filtering non-maximal subgraphs from
        bucket_of_subgraphs_with_projections = frequent_subgraphs_with_projections_split_by_size[index]
        bucket_one_bigger_of_subgraphs_with_projections = None
        #If the index is max size then there is no bucket one bigger
        if (index != len(frequent_subgraphs_with_projections_split_by_size) - 1):
            bucket_one_bigger_of_subgraphs_with_projections = frequent_subgraphs_with_projections_split_by_size[index + 1]

        # Check if there are non-maximal subgraphs in the same bucket and remove them
        bucket_of_subgraphs_with_projections = filter_nonmaximal_subgraphs_from_same_bucket(bucket_of_subgraphs_with_projections)

        if (bucket_one_bigger_of_subgraphs_with_projections is not None):
            # Check if the subgraph has a super version in the next biggest bucket and remove the subgraph
            bucket_of_subgraphs_with_projections = filter_nonmaximal_subgraphs_from_the_bucket_one_bigger(bucket_of_subgraphs_with_projections,
                                                                   bucket_one_bigger_of_subgraphs_with_projections)
        frequent_subgraphs_with_projections_split_by_size[index] = bucket_of_subgraphs_with_projections

def filter_nonmaximal_subgraphs_from_same_bucket(bucket_of_subgraphs_with_projections):
    from gspan import gSpan
    subgraph_indices_to_remove = []
    # Check if the subgraph has a super version in the same bucket
    for subgraph_and_projection_index in range(0, len(bucket_of_subgraphs_with_projections)):
        subgraph_and_projection_1 = bucket_of_subgraphs_with_projections[subgraph_and_projection_index]
        # subgraph1 = subgraph_and_projection_1[0] - not used
        projected1 = subgraph_and_projection_1[1]
        support1 = gSpan._get_support(None, projected1)

        for subgraph_and_projection_index_other in range(subgraph_and_projection_index+1,len(bucket_of_subgraphs_with_projections)):
            #Check if we are trying to use and subgraphs that were already scheduled to be removed
            if(subgraph_and_projection_index_other in subgraph_indices_to_remove):
                continue #We are going to delete the other subgraph so dont bother checking it
            elif(subgraph_and_projection_index in subgraph_indices_to_remove):
                break #We are going to delete the current subgraph so dont check it

            # initalize several local variables for simplicity
            subgraph_and_projection_2 = bucket_of_subgraphs_with_projections[subgraph_and_projection_index_other]
            # subgraph2 = subgraph_and_projection_2[0] - not used
            projected2 = subgraph_and_projection_2[1]

            # Get the support for the two subgraphs being compared now
            support2 = gSpan._get_support(None, projected2)

            # If the support of the two subgraphs are not the same then the two subgraphs cannot be subsets of each other
            if (support1 is not support2):
                # In this case we restart the inner loop and compare the initial subgraph to a different subgraph in the bucket
                continue
            else:
                # Check corresponding PDFs in both projected lists to make sure corresponding PDFs come from the same graph in the graphset
                for projected_index in range(0, len(projected1)):
                    # If the graph id of each pdfs in projected1 does not match the corresponding pdfs in projected2
                    # then one of the subgraphs is not a subset of the other graph and we can move on with our inner loop
                    if (projected1[projected_index].gid != projected2[projected_index].gid):
                        continue

                # If the projection of subgraph1 minus the head edge or minus the tail edge is equal to all of the projection of subgraph2
                # then subgraph2 is a subset of subgraph1
                tail_less_copy_of_proj_1_pdfs = create_tail_less_deep_copy_of_projection_pdfs(projected1)
                if (projected2[0] == projected1[0].prev or projected2[0] == tail_less_copy_of_proj_1_pdfs):
                    if(subgraph_and_projection_index_other not in subgraph_indices_to_remove):
                        subgraph_indices_to_remove.append(subgraph_and_projection_index_other)

                # If the projection of subgraph2 minus the head edge or tail edge is equal to all of the projection of subgraph1
                # then subgraph1 is a subset of subgraph2
                tail_less_copy_of_proj_2_pdfs = create_tail_less_deep_copy_of_projection_pdfs(projected2)
                if (projected1[0] == projected2[0].prev or projected1[0] == tail_less_copy_of_proj_2_pdfs):
                    if(subgraph_and_projection_index not in subgraph_indices_to_remove):
                        subgraph_indices_to_remove.append(subgraph_and_projection_index)

    for index in reversed(subgraph_indices_to_remove):
        del bucket_of_subgraphs_with_projections[index]
    return bucket_of_subgraphs_with_projections

def filter_nonmaximal_subgraphs_from_the_bucket_one_bigger(bucket_of_subgraphs_with_projections, bucket_one_bigger_of_subgraphs_with_projections):
    from gspan import gSpan
    num_removed = 0

    for subgraph_and_projection_index in range(0,len(bucket_of_subgraphs_with_projections)):
        # initalize several local variables for simplicity
        subgraph_and_projection_1 = bucket_of_subgraphs_with_projections[subgraph_and_projection_index - num_removed]
        # subgraph1 = subgraph_and_projection_1[0] - not used
        projected1 = subgraph_and_projection_1[1]

        # Get the support for the two subgraphs being compared now
        support1 = gSpan._get_support(None, projected1)

        for bigger_subgraph_and_projection_index in range(0, len(bucket_one_bigger_of_subgraphs_with_projections)):
            # initalize several local variables for simplicity
            subgraph_and_projection_2 = bucket_one_bigger_of_subgraphs_with_projections[bigger_subgraph_and_projection_index]
            # subgraph2 = subgraph_and_projection_2[0] - not used
            projected2 = subgraph_and_projection_2[1]

            # Get the support for the two subgraphs being compared now
            support2 = gSpan._get_support(None, projected2)

            # If the support of the two subgraphs are not the same then the the smaller subgraph cannot be subset of the bigger subgraph
            if (support1 is not support2):
                # In this case we restart the inner loop and compare the initial subgraph to a different subgraph in the bigger bucket
                continue
            else:
                # Check corresponding PDFs in both projected lists to make sure corresponding PDFs come from the same graph in the graphset
                for projected_index in range(0, len(projected1)):
                    # If the graph id of each pdfs in projected1 does not match the corresponding pdfs in projected2
                    # then one of the subgraphs is not a subset of the other graph and we can move on with our inner loop
                    if (projected1[projected_index].gid != projected2[projected_index].gid):
                        continue

                # If the projection of subgraph2 (the bigger subgraph) minus the head edge or tail edge is equal to all of the projection of subgraph1
                # then subgraph1 is a subset of subgraph2
                tail_less_copy_of_proj_2_pdfs = create_tail_less_deep_copy_of_projection_pdfs(projected2)
                if (projected1[0] == projected2[0].prev or projected1[0] == tail_less_copy_of_proj_2_pdfs):
                    del bucket_of_subgraphs_with_projections[subgraph_and_projection_index - num_removed]
                    num_removed += 1
                    break # break the inner loop

    return bucket_of_subgraphs_with_projections

def create_tail_less_deep_copy_of_projection_pdfs(projected):
    tail_less_copy_of_proj_pdfs = copy.deepcopy(projected[0])
    current = tail_less_copy_of_proj_pdfs
    if current.prev is not None:
        while (current.prev.prev is not None):
            current = current.prev
        current.prev = None

    return tail_less_copy_of_proj_pdfs

def print_subgraph_buckets(frequent_subgraphs_with_projections_split_by_size):
    for bucket in frequent_subgraphs_with_projections_split_by_size:
        if(len(bucket) > 0):
            print("Subgraphs of Size: " + str(len(bucket[0][0])))

            for subgraph in bucket:
                print(subgraph[0])