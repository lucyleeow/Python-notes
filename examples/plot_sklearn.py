# -*- coding: utf-8 -*-
"""
Scikit-learn
###############

"""

#%%
# Preprocessor methods
# ********************
#
# Preprocessors have the methods ``fit`` and ``transform`` and are named to fit
# with scikit learn API. ``fit()`` does not actually mean 'fitting the data'
# like it does for model functions, which have the methods ``fit()`` and
# ``predict()``.
#
# For preporcessing functions, ``fit()`` simply signifies a method that is
# performed on the training data and it takes both features and target as
# arguments (this allows you to use the training target during preprocessing,
# e.g., to do target encoding). It calculates parameters, saves them as
# attributes of ``self``. It also returns ``self``, which is not technically
# required as changing self will allow the new self attributes to be available
# but it is done so that you can chain functions together (e.g.,
# ``.fit().transform()``). This is because if you do not return anything,
# ``None`` is returned by default. If you look at the source code, ``fit()`` of
# ``OrdinalEncoder`` returns a list of categories and their corresponding
# number. This is used in ``transform()`` to 'ecode' a column of categories into
# numbers. ``transform()`` (like ``predict()``) is performed on both training
# and test datasets.
#
# The implication of ``fit()`` being only performed on the training data and
# ``transform()`` being performed on both training and test (in a typical
# pipeline) is that the preprocessing parameters are calculated on the training
# dataset. For example, if you are 'imputting' missing values by replacing them
# with the median, missing values in both the training and test dataset will be
# replaced by the median value from the training dataset. If you are using
# ordinal encoding, only the categories present in the training dataset will be
# available (as an attribute of ``self``). Thus, if there is a category present
# in the test dataset but not the training dataset, it will not be recognised
# and will need to be dealt with some other way. For this specific issue, at the
# moment ``OneHotEncoder()`` has a ``handle_unknown`` parameter,
# ``OrdinalEncoder()`` does not.
#
# Writing your own transformer class
# **********************************
#
# Scikit learn preprocessors, called 'transformers' (e.g., `OneHotEncoder`), are
# classes. You use them by creating an instance of the class. The class has to
# have the methods ``fit`` ``transform``, ``fit_transform``, ``get_params`` etc.
# To avoid writing all these methods, you can code what you want in your
# transformer and inherit everything else from a base class.
#
# A simple way to get a transformer that does not require a ``fit`` method is to
# use the function ``FunctionTransformer()``. This is called a 'stateless'
# transformer as no parameters need to be saved from ``fit`` and a function is
# simply performed on both the training and test datasets. For example,
# multiplying all the values of a column by a value.
#
# More complex tranformers can be created by inheriting from the class
# ``BaseEstimator``, which allows you to get ``get_params`` and ``set_params``
# for free. ``TransformerMixin`` allows you to get ``fit_transform`` for free
# when we define ``fit`` and ``transform``.
#
# Pipelines
# *********
#
# A pipeline is essentially a list of transformers and a final estimator. The
# purpose is to allow you to neatly assemble a pipeline that can be given to a
# cross validation function. This way you can alter parameters of transformers
# in your pipeline and cross validate, easily. It also simplifies proprocessing
# by allowing you to easily ensure parameters are calculated using the training
# data and not the testing data.
#
# When you call ``fit`` on your pipeline, it is calling ``fit_transform`` on all
# the transformer steps and ``fit`` on the final modelling step. When you
# perform this on your training data, it preprocesses all the data and fits a
# model to the full transformed data. When you call ``predict`` or
# ``predict_proba`` on your pipeline, it performs ``transform`` on all the
# transform steps and ``predict`` on the final model step. If you perform this
# on your testing data, it preprocesses your test data (using states calculated
# on your training data and saved) then uses the data and the fitted model to
# give predictions.
#
# ColumnTransformer
# ================
#
# This function allows you to perform specific transformations on specific
# columns. The output is concatenated together at the end. For each step in the
# ``ColumnTransformer`` the input is the specified columns of your dataset,
# which undergoes a pipeline of transformer(s) and the output is the result of
# the transformations.
#
# Let's take a complex example to further explore how ``ColumnTransformer``
# works. If one of your transformations was to merge a separate dataset, you
# could define a merge function, use ``FunctionTransformer`` to create a sklearn
# compatible transformer and then add it as a step to ``ColumnTransformer``. If
# you wanted to then transform columns from the new merged dataset, you would
# need to have a second ``ColumnTransformer`` within the first
# ``CoumnTransformer``.
#
#
#

# %%
