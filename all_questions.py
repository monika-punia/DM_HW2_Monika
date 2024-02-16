# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.0
    level1["smoking_info_gain"] = 0.2780

    level1["cough"] = - 1.0
    level1["cough_info_gain"] = 0.2364

    level1["radon"] = - 1.0
    level1["radon_info_gain"] = 0.0348

    level1["weight_loss"] = - 1.0
    level1["weight_loss_info_gain"] = 0.0290

    level2_left["smoking"] = - 1.0
    level2_left["smoking_info_gain"] = 0.0
    level2_right["smoking"] = - 1.0
    level2_right["smoking_info_gain"] = 0.0

    level2_left["radon"] = - 1.0
    level2_left["radon_info_gain"] = 0.07290

    level2_left["cough"] = 1.0
    level2_left["cough_info_gain"] = 0.72192

    level2_left["weight_loss"] = - 1.0
    level2_left["weight_loss_info_gain"] = 0.1709

    level2_right["radon"] = 1.0
    level2_right["radon_info_gain"] = 0.7219

    level2_right["cough"] = - 1.0
    level2_right["cough_info_gain"] = 0.32192

    level2_right["weight_loss"] = - 1.0
    level2_right["weight_loss_info_gain"] = 0.17095

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    tree = u.BinaryTree("smoking")  # MUST STILL CREATE THE TREE *****
    A = tree.insert_left("cough")
    B = tree.insert_right("radon")
    A.insert_left("Yes")
    A.insert_right("No")
    B.insert_left("Yes")
    B.insert_right("No")
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0  

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}


    # Answers are floats
    answer["(a) entropy_entire_data"] = 0.
    # Infogain
    answer["(b) x <= 0.2"] = 0.
    answer["(b) x <= 0.7"] = 0.
    answer["(b) y <= 0.6"] = 0.

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = ""  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("Root")
    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    

    # float
    answer["(a) Gini, overall"] = 0.5

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.48
    answer["(d) Gini, Car type"] = 0.1625
    answer["(e) Gini, Shirt type"] = 0.4914

    answer["(f) attr for splitting"] = "Car type"

    # Explanatory text string
    answer["(f) explain choice"] = "The Car type attribute has the lowest Gini index, suggesting that it leads to more pure subsets after splitting. This makes it the best choice for the root node in our analysis."
    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ['binary','qualitative','ordinal']

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = "Time, categorized as either AM or PM, is a binary qualitative attribute that falls into two clear categories."

    answer["b"] = ['continuous','quantitative','ratio']
    answer["b: explain"] = "The brightness, as assessed by a light meter, is a quantitative attribute that exists on a continuous scale with ratio properties."

    answer["c"] = ['discrete','qualitative','ordinal']
    answer["c: explain"] = "People's judgments of brightness can be seen as a continuous, qualitative attribute with an ordinal nature, reflecting subjective perceptions arranged by intensity."

    answer["d"] = ['continuous','quantitative','ratio']
    answer["d: explain"] = "Angles, quantified in degrees within the range of 0 to 360, are continuous quantitative attributes that indicate ratios on a scale."

    answer["e"] = ['discrete','qualitative','ordinal']
    answer["e: explain"] = "The Olympic medals, categorized as Bronze, Silver, and Gold, are discrete qualitative attributes arranged in order based on rank."

    answer["f"] = ['continuous','quantitative','interval']
    answer["f: explain"] = "Height above sea level is a continuous quantitative attribute, potentially interval or ratio if ratios between heights are meaningful and sea level serves as an arbitrary origin."
    answer["g"] = ['discrete','quantitative','ratio']
    answer["g: explain"] = "The count of patients in a hospital is a discrete quantitative attribute, measurable on a ratio scale."

    answer["h"] = ['discrete','qualitative','nominal']
    answer["h: explain"] = "ISBN numbers assigned to books are discrete qualitative attributes, serving as unique identifiers without any inherent order."

    answer["i"] = ['discrete','qualitative','ordinal']
    answer["i: explain"] = "The ability to transmit light, classified as opaque, translucent, or transparent, is a qualitative attribute with discrete categories, arranged in ascending order based on increasing light transmission."

    answer["j"] = ['discrete','qualitative','ordinal']
    answer["j: explain"] = "Military rank is a qualitative attribute with discrete categories, organized hierarchically from the lowest to the highest rank."

    answer["k"] = ['continuous','quantitative','ratio']
    answer["k: explain"] = "The distance from the campus center is a continuous quantitative attribute, potentially interval or ratio if the campus center is considered an arbitrary origin and ratios between distances are meaningful."

    answer["l"] = ['discrete','quantitative','ratio']
    answer["l: explain"] = "The substance's density, measured in grams per cubic centimeter, is a continuous quantitative attribute, assessable on a ratio scale."

    answer["m"] = ['discrete','qualitative','nominal']
    answer["m: explain"] = "Coat check number is a discrete qualitative attribute, representing distinct categories without intrinsic order."

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = " Model 2 is expected to perform better on unseen instances as it maintains similar accuracies on both datasets, indicating superior generalization compared to Model 1, where the drop in accuracy from Dataset A to B suggests overfitting."
    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = "Even though Model 2 is a bit less accurate, it's still a better choice because it generalizes well and is less likely to overfit. In contrast, Model 1 had a big drop in accuracy on Dataset B."
    explain["c similarity"] = "Regularization Approach to Avoid Overfitting"
    explain["c similarity explain"] = "Both methods use penalties to stop models from fitting too closely to the training data. MDL penalizes complex models by considering encoding cost. Pessimistic error penalizes complexity by adjusting for errors."
    explain["c difference"] = "Model Optimization Criterion"
    explain["c difference explain"] = "MDL aims to minimize description length, preferring simpler models that encode data more concisely.Pessimistic error aims to minimize penalized error rate directly, by adjusting error higher for more complex models."


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = ""
    answer["a, level 2, right"] =""
    answer["a, level 2, left"] = ""
    answer["a, level 3, left"] = ""
    answer["a, level 3, right"] = ""

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("root note")

    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

  
    # float
    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.531

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.231
    answer["e, gain ratio, Handedness"] = 0.531

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

