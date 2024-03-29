import os
import subprocess
        
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

ith open(job_file,'w') as fh: #create slurm batch script
    fh.writelines('#!/bin/csh\n')
    fh.writelines('#SBATCH --time='+time+'\n')
    fh.writelines('#SBATCH -o slurm-%j.out-%N'+'\n')
    fh.writelines('#SBATCH -e slurm-%j.err-%N'+'\n')
    fh.writelines('#SBATCH --nodes='+str(nnodes)+'\n')
    fh.writelines('#SBATCH --ntasks='+str(ntasks)+'\n')
    fh.writelines('#SBATCH --account='+account+'\n')
    fh.writelines('#SBATCH --partition='+partition+'\n')
    fh.writelines('#SBATCH -M'+cluster+'\n')
    if mem is not None:
        fh.writelines('#SBATCH --mem='+mem+'\n')
    fh.writelines('setenv WORKDIR '+wd+'\n')
    fh.writelines(module+'\n')
    fh.writelines(moduleload+'\n')
    fh.writelines(conda+'\n')
    fh.writelines('python ' + pyfile)

subprocess.run(["sbatch","--export=NONE",job_file]) #Submit python file via slurm batch script
