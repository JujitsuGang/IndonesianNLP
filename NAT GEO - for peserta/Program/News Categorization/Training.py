from __future__ import division
import Preprocessing
import NaiveBayes
import xlrd
import openpyxl
import FeatureSelection

__author__ = 'undeed'


def train(filename):

    fileTrain = xlrd.open_workbook(filename)
    dataTrain = fileTrain.sheet_by_index(0)