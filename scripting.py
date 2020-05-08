import pandas as pd
import re
import shutil
import os
from glob import glob

# Co-op isn't rated properly

rundir = os.getcwd()

def photo_move(soft=False):
    os.chdir('/Volumes/wwwroots/thelittlethingswemiss/photography')
    for f in [x for x in os.listdir('.') if 'jpg' in x]: 
        
        nf = re.sub("['%@#]", '', f) 
        nf = re.sub("!_! Green", '!_! Cover', nf) 
        
        cuts = nf.split('>') 
        cuts = [x.strip() for x in cuts] 
        second_cuts = re.split(' !_! ', cuts[-1]) 
        fcuts = cuts[:-1] 
        fcuts.extend(second_cuts) 
        np = os.path.join(*fcuts)
        
        if len(second_cuts) != 2: 
            print(f, cuts, second_cuts) 
            break 
            
        # -2 check
        tail = np.split('_')[-1]
        if '-' in tail:
            tail = re.sub('(.*)-([0-9]+).jpg', '-\g<2>_\g<1>.jpg', tail)
            np = '_'.join(np.split('_')[:-1])+tail
        
        # Space Clear
        np = re.sub(' ', '_', np) 
        
        # Make Dirs
        dirname = os.path.dirname(np) 
        os.makedirs(dirname, exist_ok=True) 
        
        if 'Cover' in np:
            coverless = '_'.join(os.path.basename(np).split('_')[1:])
            for im in glob(os.path.dirname(np)+'/*'):
                # Rename existing Cover
                if 'Cover' in im and tail in im:
                    rn = '_'.join(os.path.basename(im).split('_')[1:])
                    rn = os.path.join(os.path.dirname(im), rn)
                    if soft:
                        print("Will Rename: ", im, rn) 
                    else:
                        shutil.move(im, rn)
            for im in glob(os.path.dirname(np)+'/*'):
                # Remove coverless version
                if coverless in im and 'Cover' not in im:
                    if soft:
                        print("Will Remove: "+im) 
                    else:
                        os.remove(im)
    
        if soft:
            print(f, np) 
        else:
            shutil.move(f, np) 
        
def index():
    os.chdir('/Volumes/wwwroots/thelittlethingswemiss/photography')
    dfog = pd.DataFrame(columns=["CONTAINING", "SHOOT", 'FNAME', 'SHOOT_NUM', 'FNAME_OG', 'FULL_OG'])
    df2k = pd.DataFrame(columns=["CONTAINING", "SHOOT", 'FNAME', 'SHOOT_NUM', 'FNAME_2K', 'FULL_2K'])
    for root, dirs, files in os.walk('.'):
        if len([x for x in files if 'jpg' in x]) == 0 or root == '.':
            continue
        for f in [x for x in files if 'jpg' in x]:
            containing_dir = re.sub('^./', '/photography/', root)
            basename = '.'.join(f.split('.')[:-1]).split('_')
            resolution = basename[-1]
            basename = '_'.join(basename[:-1])
            shoot_num = basename.split('_')[-1]
            if '_2k.' in f:
                shoot_dir = root.split('/')[-1]
                shoot_dir = '.'.join(root.split('/')[-2:])
                fname = f
                full_path = os.path.join(containing_dir, fname)
                res = pd.Series({
                    'CONTAINING':containing_dir, 
                    'SHOOT':shoot_dir, 
                    'SHOOT_NUM':shoot_num, 
                    'FNAME':basename, 
                    'FNAME_2K':fname, 
                    'FULL_2K':full_path})
                df2k = df2k.append(res, ignore_index=True)
            elif '_original.' in f:
                shoot_dir = root.split('/')[-1]
                shoot_dir ='.'.join(root.split('/')[-2:])
                fname = f
                full_path = os.path.join(containing_dir, fname)
                res = pd.Series({
                    'CONTAINING':containing_dir, 
                    'SHOOT':shoot_dir,
                    'SHOOT_NUM':shoot_num,  
                    'FNAME':basename, 
                    'FNAME_OG':fname, 
                    'FULL_OG':full_path})
                dfog = dfog.append(res, ignore_index=True)
    df = dfog.merge(df2k, on=list(set(dfog.columns) & set(df2k.columns)), how='outer').reset_index(drop=True)
    
    # Cover Flag
    df['COVER'] = df.apply(lambda x: 'Cover' in x.FNAME,axis=1)
    
    # TODO Check for only having one file size in a row
    
    df.to_csv(os.path.join(rundir, '_data/photo_index.csv'))
    return df, dfog, df2k
    
def build(rm=False):
    
    if rm:
        os.chdir('/Volumes/wwwroots/thelittlethingswemiss')
        fs = [x for x in os.listdir() if 'photography' not in x]
        for f in fs:
            # print(f'rm -r {f}')
            os.system(f'rm -r {f}')
    
    os.chdir('/Users/bill/Code/thelittlethingswemiss')
    os.system('bundler exec jekyll build')
    os.system('cp -r _site/* /Volumes/wwwroots/thelittlethingswemiss/')
    
# for i, row in key.iterrows(): 
#     x = row['SHOOT'] 
#     y = row['NEW'] 
     
#     if x == y: 
#         continue 
     
#     success = False 
#     matches = 0 
#     for file in os.listdir('.'): 
#         open_file = open(file,'r') 
#         read_file = open_file.read() 
#         edited = re.sub(f'shoot_id: {x} *\n', f'shoot_id: {y}\n', read_file) 
#         if edited != read_file: 
#             success = True 
#             matches+=1 
#             write_file = open(file,'w') 
#             write_file.write(edited) 
#     if not success: 
#         print(i, x,y,"Failed") 
#         fails.append(i) 
#     if matches>1: 
#         print(i, x,y,"multimatched") 