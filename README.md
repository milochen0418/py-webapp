# Pynecone Examples for pynecone tag v0.1.28

A repository full of Pynecone example apps.

This is a special branch of from the official examples.
with the pynecone offical release 0.1.28. [open here](https://github.com/pynecone-io/pynecone/releases/tag/v0.1.28)

You can run with the following setting
```
python==3.11.?
bun==0.5.9 
node>=16.6.0  
```
```
conda create -n newenv python=3.11
conda activate newenv
```

```
cd <some-example1>
rm -rf .web && for i in $(find ./ | grep __pycache__$); do rm -rf $i; done && pip install -r requirements.txt && pc init && pc run  
cd ..

cd <some-example2>
rm -rf .web && for i in $(find ./ | grep __pycache__$); do rm -rf $i; done && pip install -r requirements.txt && pc init && pc run  
cd ..

```


```
conda deactivate 
```