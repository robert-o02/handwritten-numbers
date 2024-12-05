from torchvision import  datasets
from torchvision.transforms import ToTensor
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# getting data

train_data = datasets.MNIST(
        root = 'data',
        train = True,
        transform = ToTensor(),
        download = False
        )

test_data = datasets.MNIST(
        root = 'data',
        train = False,
        transform = ToTensor(),
        download = False
        )
