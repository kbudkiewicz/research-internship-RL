import numpy as np
from matplotlib import pyplot as mpl
from collections import deque
import data as d

def into_matrix(*args):
    # input is a tuple of lists (*args) from each run
    # find the maximum length
    amount = len(args)
    l = []
    for i in range(amount):
        l.append( len(args[i]) )
    min_len = l[np.argmin(l)]
    # matrix = np.eye(amount, min_len)

    # with max_length
    max_len = l[np.argmax(l)]
    matrix = np.eye(amount, max_len)

    for i in range(amount):
        if len( args[i] ) < max_len:
            while len( args[i] ) < max_len:
                args[i].append(None)

    # append each list to the matrix
    for i in range(amount):
        # matrix[i, :] = args[i][0:min_len]
        matrix[i, :] = args[i][0:max_len]

    return matrix

def lin_var_plot(matrices, labels, title="NO_TITLE_FOUND"):
    # input an iterable of matrices to diagnose
    mpl.figure()
    for matrix in matrices:
        if type(matrices) == list:
            matrix_width = matrix.shape[1]
        else:
            matrix_width = matrices.shape[1]
            matrix = matrices
        x = np.arange(matrix_width)

        # extract data and calculate means and standard deviations at each column
        means = []
        sdevs = []
        for i in range(matrix_width):
            if matrix[:,i].any() == None:
                continue
            else:
                means.append( np.mean(matrix[:,i]) )
                sdevs.append( np.sqrt(np.var(matrix[:,i])) )

        # redefine means as a moving average of last 100 values
        moving_avg = deque(maxlen=100)
        for i in range(matrix_width):
            moving_avg.append(means[i])
            means[i] = np.mean(moving_avg)

        # define the position of the contours
        top = []
        bottom = []
        for i in range(matrix_width):
            top.append( means[i]+sdevs[i] )
            bottom.append( means[i]-sdevs[i] )

        mpl.fill_between(x, top, bottom, alpha=0.3, label='_nolegend_')
        mpl.plot(x,means)

    mpl.title(title)
    mpl.xlabel('Episode #')
    mpl.ylabel('Averaged score at given episode')
    mpl.legend(labels=labels, loc = 'lower right')
    mpl.show()


### selective plotting
# comparison untrained vs imported state_dict
# labels = ('Untrained','Trained')
# lin_var_plot( [d.M_n2_s, d.M_sd_s], labels)
# lin_var_plot( [d.M_n2_l, d.M_sd_l], labels )

# amount of hidden layers comparison
labels = ('3 hidden layers', '4 hidden layers', '5 hidden layers')
lin_var_plot( [d.M_n2_s, d.M_hl4_s, d.M_hl5_s], labels, title='Moving score average across different hidden layer sizes' )
# lin_var_plot( [d.M_n2_l, d.M_hl4_l, d.M_hl5_l], labels, title='Moving loss average across different hidden layer sizes')

# amount of neurons comparison
# labels = ('32 neurons', '64 neurons', '128 neurons', '256 neurons')
# lin_var_plot([d.M_n1_s, d.M_n2_s, d.M_n3_s, d.M_n4_s], labels, title='Moving score average across different neuron amount')
# lin_var_plot([d.M_n1_l, d.M_n2_l, d.M_n3_l, d.M_n4_l], labels, title='Moving loss average across different neuron amount')

# epsilon comparison
# labels = ('epsilon = 0.995','epsilon = 0.9975','epsilon = 0.999')
# lin_var_plot([d.M_e995_s, d.M_e9975_s, d.M_e999_s], labels)
# lin_var_plot([d.M_e995_l, d.M_e9975_l, d.M_e999_l], labels)
