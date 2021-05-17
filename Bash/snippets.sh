grep -Eoi pattern file # get strings matching patterns (-E: --extended-regexp, -o: --only-matching, -i: --ignore-case)
$(cmd) # cmd result as variable
for var in "$@" # iterate arguments. can also use: for i;
bs=8; for ((i=0; i<=$#; i+=bs)); do echo "${@:i:bs}"; done # iterating over batches of the arguments. for array, replace `$#`` with `${#s[@]}` and `@` with `s[@]`
read -a s <<< "$@" # arguments into array
grep -Eoi '<A [^>]+>' file | grep -Eoi 'HREF="[^\"]+"' |  grep -Eo '(http|https)://[^"]+') # get links from html file
rsync -avh <source> <dst> # merge folders 
man -K <keyword> # search in man pages for keyword
pip uninstall -y -r <(pip freeze) # reset all pip packages
find -name <regex-like>
pkill -f <my_pattern> # kill proccess with partial name
# CTRL+ALT+E -  expand alias
