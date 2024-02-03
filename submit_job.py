import os
import subprocess
import make_slurm
        
job_file = #Job File
account = #Account
partition = #Partition
cluster = #Cluster
mem = #Memory
time = #Time
nnodes = #Number of Nodes
ntasks = #Number of Tasks
wd = '$HOME'
module = 'module use $HOME/MyModules/' 
moduleload = 'module load miniconda3/latest' #Can replace with different module loading
conda = 'conda activate ' + #Environment Name
ipynb = False
ipynbf = 'cds_cmip6_download.ipynb'

if ipynbf[-6:-1] == 'ipynb':
    ipynb == True
else:
    pyfile = ipynbf
    
if ipynb == True: #turn Jupyter notebook into python file
    subprocess.run(['jupyter','nbconvert', '--to','script', ipynbf])
    pyfile = ipynbf[:-5]+'py'
    
subprocess.run(['chmod','755',pyfile]) #Makes file executable

subprocess.run(["sbatch","--export=NONE",job_file]) #Submit python file via slurm batch script
