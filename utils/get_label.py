
# import numpy as np
# def get_closest_label(color, reference_dict):
#     def distance(c1, c2):
#         return np.sqrt(np.sum((np.array(c1) - np.array(c2)) ** 2))

#     min_distance = float('inf')
#     closest_label = None

#     for label, ref_colors in reference_dict.items():
#         for ref_color in ref_colors:
#             d = distance(color, ref_color)
#             if d < min_distance:
#                 min_distance = d
#                 closest_label = label

#     return closest_label
