# -*- coding: utf-8 -*-
"""
Scikit-learn
###############

"""

#%%
# ``fit()``` and ``transform()``
# ******************************
#
# The functions are named to fit with scikit learn API. ``fit()`` does not
# actually mean 'fitting the data' like it does in ``fit()`` and ``predict()``
# for model functions. The ``fit()`` and ``transform()`` functions of
# preprocessing functions (e.g., ``OrdinalEncoder()`` and ``OneHotEncoder()``).
# ``fit()`` means that it is performed on the training data and it can take
# both features and target as arguments (this allows you to use the training
# target column during preprocessing, e.g., to do target encoding). It
# calculates parameters, saves them as attributes of ``self``. It also
# returns ``self``, which is not technically required as simply changing self
# will carry forward the changes but is done so that you can chain functions
# together (e.g., ``.fit().transform()``), as if you do not return anything,
# ``None`` is returned by default. If you look at the source code, ``fit()`` of
# ``OrdinalEncoder`` returns a list of categories and their corresponding
# number. This is used in ``transform()`` to 'ecode' a column of categories
# into numbers. ``transform()`` (like ``predict()``) is/can be performed on
# both training and test dataset.
#
# The implication of ``fit()`` being only performed on the training data
# and ``transform()`` being performed on both training and test (in a typical
# pipeline) is that the values being calculated on the training dataset.
# For example, if you are 'imputting' missing values by replacing them with
# the median, missing values in both the training and test dataset will be
# replaced by the median value from the training dataset. If you are using
# ordinal encoding, only the categories present in the training dataset will
# be available (as an attribute of ``self``). Thus, if there is a category
# present in the test dataset but
# not the training dataset, it will not be recognised and will need to be dealt
# with some other way.
# For this specific issue, at the moment ``OneHotEncoder()`` has a
# ``handle_unknown``
# parameter, ``OrdinalEncoder()`` does not.
#
# Writing your own transformer class
# **********************************
#
# Scikit learn transformers (e.g., `OneHotEncoder`) are classes. You use them
# by creating an instance of the class. The class has to have the methods
# ``fit`` ``transform``, ``fit_transform``, ``get_params`` etc. To avoid writing
# all these methods, you can code what you want in your transformer and
# inherit everything else from a base class.
#
# ``BaseEstimator`` allows us to get ``get_params`` and ``set_params`` for
# free and ``TransformerMixin`` allows us to get ``fit_transform`` for free
# when we define ``fit`` and ``transform``. -
#
#
#
#

# %%
