USE_CUDA = False  # True
RESTORE = True  # False
TEACHER_RATIO = 0.5
MAX_LENGTH = 32
TARGET_LENGTH=5
MODEL_DIR = "./model_201905131"
PRE_MODEL_DIR="./model_pre"
LOSS_DIR="PIC"
CLIP = 5.0
LR = 0.00005  #

ATT_MODEL = 'general'
HIDDEN_SIZE = 1024
NUM_LAYER = 2
DROPOUT = 0.005  # 0.001

NUM_ITER = 2000
PLOT_STEP = 10
PRINT_STEP = 10
CHECKPOINT_STEP = 200  # 2000
BATCH_SIZE = 32
