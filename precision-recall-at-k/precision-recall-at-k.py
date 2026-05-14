def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    is_relevant = dict.fromkeys(relevant, True)
    intersection = 0
    for i in range(k):
        if recommended[i] in is_relevant:
            intersection += 1
    precision = intersection / k
    recall = intersection / len(relevant)
    return [precision, recall]
    # Write code here