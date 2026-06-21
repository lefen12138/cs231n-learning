from builtins import range
import numpy as np
from random import shuffle
xrange = range


def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    # compute the loss and the gradient
    num_classes = W.shape[1]
    num_train = X.shape[0]
    for i in range(num_train):
        scores = X[i].dot(W)

        # compute the probabilities in numerically stable way
        scores -= np.max(scores)
        p = np.exp(scores)
        p /= p.sum()  # normalize
        logp = np.log(p)

        #grad 
        dscores = p.copy()
        dscores[y[i]] -= 1  # derivative of loss w.r.t. scores
        dW += np.outer(X[i], dscores)  # chain rule to get gradient

        loss -= logp[y[i]]  # negative log probability is the loss


    # normalized hinge loss plus regularization
    loss = loss / num_train + 0.5 * reg * np.sum(W * W)
    dW /= num_train
    dW += reg * W  # derivative of regularization term

    #############################################################################
    # TODO:                                                                     #
    # Compute the gradient of the loss function and store it dW.                #
    # Rather that first computing the loss and then computing the derivative,   #
    # it may be simpler to compute the derivative at the same time that the     #
    # loss is being computed. As a result you may need to modify some of the    #
    # code above to compute the gradient.                                       #
    #############################################################################


    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    N, D = X.shape
    #计算样本得分
    scores = X.dot(W)

    max_scores = np.max(scores, axis=1, keepdims=True)
    # axis=1：按每行求和（每个样本所有类别） 
    # keepdims=True：保持二维形状，保证广播除法正常执行
    scores -= max_scores  # 数值稳定性,softmax函数对输入进行平移不会改变输出
    exp_scores = np.exp(scores)
    sum_exp_scores = np.sum(exp_scores, axis=1, keepdims=True)
    probs = exp_scores / sum_exp_scores  # 计算概率

    correct_probs = probs[np.arange(N), y]  # 获取正确类别的概率
    loss = -np.sum(np.log(correct_probs)) / N

    # 4. 加上 L2 正则损失
    reg_loss = 0.5 * reg * np.sum(W * W)
    loss = loss + reg_loss

    # ---------------------- 梯度 dW 向量化计算 ----------------------
    # 对每个样本：dscores = probs - 1(真实类别位置)
    dscores = probs.copy()
    dscores[np.arange(N), y] -= 1
    dscores /= N

    # dW = X^T · dscores
    dW = X.T.dot(dscores)

    # 加上正则项梯度
    dW += reg * W
    #############################################################################
    # TODO:                                                                     #
    # Implement a vectorized version of the softmax loss, storing the           #
    # result in loss.                                                           #
    #############################################################################


    #############################################################################
    # TODO:                                                                     #
    # Implement a vectorized version of the gradient for the softmax            #
    # loss, storing the result in dW.                                           #
    #                                                                           #
    # Hint: Instead of computing the gradient from scratch, it may be easier    #
    # to reuse some of the intermediate values that you used to compute the     #
    # loss.                                                                     #
    #############################################################################


    return loss, dW
