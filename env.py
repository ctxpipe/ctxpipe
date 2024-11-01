import os
import warnings
from typing import Literal

import numpy as np
import torch

import deterministic
from ctxpipe.env.primitives import *


def init():
    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    deterministic.seed_everything()

    np.set_printoptions(suppress=True)
    torch.set_printoptions(sci_mode=False)

    warnings.filterwarnings("ignore")

    from config import default_config as conf

    conf.makedirs()


IS_TEST = "TEST" in os.environ and os.environ["TEST"] != 0
DEVICE = torch.device("cuda")

supported_model = [
    "RandomForestClassifier",
    "KNeighborsClassifier",
    "LogisticRegression",
    "SVC",
    "MLPClassifier",
]


eval_predictor_id = 2
eval_predictor_name = supported_model[eval_predictor_id]

exp_prefix: str = f"exp"
