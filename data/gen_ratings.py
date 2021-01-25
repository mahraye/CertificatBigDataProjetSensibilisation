import numpy as np
import sys

"""
Generates a rating file with given size
"""


def float_to_rate(x):
    """
    Converts a float to a rate between 1 and 5

    Inputs:
      x: a float in ]-inf, inf[
    Outputs:
      r: an int in {1,2,..,5}
    """

    y = np.arctan(x)/np.pi + 0.5  # in ]0, 1[
    r = np.floor(1 + 5*y)
    return r


def rating_matrix(m, n, k, std):
    """
    Generates a rating matrix

    Inputs:
      m: number of individuals
      n: number of films
      k: rank
      std: Gaussian noise standard deviation
    Outputs:
      R: a m by n matrix containing the rates
    """

    P = np.random.randn(m, k)
    Q = np.random.randn(n, k)
    E = std*np.random.randn(m, n)
    R = np.dot(P, Q.T) + E
    return float_to_rate(R)


def rating_matrix_to_file(R, file_name, start_UserID, start_MovieID):
    """
    Writes a rating matrix to a file in the format
    UserID::MovieID::Rating

    Inputs:
      R: the rating matrix
      filename: the name of the file to be appended or created
      start_UserID: the ID of the first user
      start_Movie: the ID of the first movie
    Outputs:
      the file on disk
    """

    with open(file_name, 'a+') as file:
        for i in range(R.shape[0]):
            for j in range(R.shape[1]):
                UserID = str(i+start_UserID)
                MovieID = str(j+start_MovieID)
                Rating = str(int(R[i, j]))
                line = UserID + "::" + MovieID + "::" + Rating + "\n"
                file.write(line)


def gen_ratings(file_name="ratings.dat",
                m=100, n=50, k=10, std=1,
                start_UserID=1, start_MovieID=1):
    """
    Combines the previous functions
    """

    R = rating_matrix(m, n, k, std)
    rating_matrix_to_file(R, file_name, start_UserID, start_MovieID)


if __name__ == "__main__":
    gen_ratings(*sys.argv[1:])
