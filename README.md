# Anaconda
## Anaconda 安装环境
```
conda create -p <your path> python==<your python version>
```
## 基本使用
```
conda activate <your path>
```

### anaconda换源
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/

conda config --remove channels <your channel>

conda config --show channels

conda config --append channels conda-forge
```

```

deactivate

conda env list

conda list

conda env remove --name myenv

conda install <package_name>
```

# Jupyter notebook

## Jupyter 基本安装与使用
``` 
conda install jupyter

jupyter-notebook --generate-config
```

## Jupyter 更换内核
```
conda activate <your env>
python -m ipykernel install --name <your env>
```
