import subprocess



def runcmd(cmd, verbose = False, *args, **kwargs):

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass

if __name__=='__main__':
   #runcmd('echo "Hello, World!"', verbose = True)
   with open("url_to_download.txt") as fp:
       for line in fp:
           print(line)
           x="wget --directory-prefix=taxi_data_par "+line+".parquet"
           print(x)
           #runcmd("cd /", verbose=True)
           runcmd(x,verbose=True)
