BASH script

"assno3-1"
for (( c=808; c<=8008; c++ ))
do
echo "TR- $c"
done

"assno3-2"
alias trestles="ssh wamurchi@trestles.uark.edu"
alias cl="clear"
alias pd="pwd"

"assn03-3"
ls -l | grep -c fasta
15085 
ls -l | grep fasta

"assn03-4"
ls -l | grep -c tre
14640
ls -l | grep tre

"assn03-5"
ls -l | grep -c sched
15262
ls -l | grep sched

"assn03-6"
445

for i in *.fasta
do
	#echo $i ${i%.fasta}_raxml.tre
	if [ -e ${i%.fasta}_raxml.tre ] 
	then 
	continue
	else 
	echo $i "_raxml.tre not found"
	fi 
done

"assn03-7"
for i in *.sched
do 
ls -l | grep "Program Return Code: 0" $i | uniq | wc -l >> grep_results.txt
done

grep "0" grep_results.txt | wc -l
42

"assn03-8"

for i in *.fasta
do
	#echo $i ${i%.fasta}_raxml.tre
	if [ -e ${i%.fasta}_raxml.tre ] 
	then 
	continue
	else 
	write_raxml_job_script.py $i
	fi 
done
