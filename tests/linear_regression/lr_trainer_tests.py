import machine_learning.linear_regression.linear_regression as lr
import machine_learning.linear_regression.lr_trainer as trainer
import tests.test_data.lin_reg_data as test_data
import numpy as num_py
import unittest
import sys


class TestLinearRegressionTrainerTest(unittest.TestCase):

    def test_train_lr_function(self):
        """
        In this test we check whether the cost value is consistently decreasing

        :return:
        """
        alpha = 0.001
        lambda_reg = 0.01
        no_of_iterations = 5
        linear_regression = lr.LinearRegression(alpha, no_of_iterations, lambda_reg)
        trainer_object = trainer.LinearRegressionTrainer(linear_regression)
        [j_history, theta] = trainer_object.train(test_data.TRAINER_TEST_X, test_data.TRAINER_TEST_Y)
        previous_value = sys.maxint
        flag = True
        for x, value in num_py.ndenumerate(j_history):
            if previous_value <= value:
                flag = False
            previous_value = value
        self.assertEqual(True, flag)

    def test_linear_regression_predictor(self):
        """
        We train the neural network and do the prediction

        :return:
        """
        alpha = 0.001
        lambda_reg = 0.01
        no_of_iterations = 15
        linear_regression = lr.LinearRegression(alpha, no_of_iterations, lambda_reg)
        trainer_object = trainer.LinearRegressionTrainer(linear_regression)
        [j_history, theta] = trainer_object.train(test_data.TRAINER_TEST_X, test_data.TRAINER_TEST_Y)
        prediction_1 = trainer.LinearRegressionTrainer.predict(test_data.TRAINER_TEST_VALUE_1, theta)
        prediction_2 = trainer.LinearRegressionTrainer.predict(test_data.TRAINER_TEST_VALUE_2, theta)
        self.assertEqual(prediction_1.item(0), test_data.TRAINER_TEST_PREDICTION_1)
        self.assertEqual(prediction_2.item(0), test_data.TRAINER_TEST_PREDICTION_2)
