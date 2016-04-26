This is the README for condructing the toy data

I took 10 total genomes of the E. Coli genome from the NCBI website.  This was the search.

Escherichia coli[ORGN] K-12[STRN]

Genomes GI's I took
985533865 (data stored in: ecoli1.wg.gbk)
985000614 (data stored in: ecoli2.wg.gbk)
983515101 (data stored in: ecoli3.wg.gbk)
937526251 (data stored in: ecoli4.wg.gbk)
937521852 (data stored in: ecoli5.wg.gbk)
937517453 (data stored in: ecoli6.wg.gbk)
749204315 (data stored in: ecoli7.wg.gbk)
938151181 (data stored in: ecoli8.wg.gbk)
938149557 (data stored in: ecoli9.wg.gbk)
938151182 (data stored in: ecoli10.wg.gbk)

I made each genome a fasta file and then split the genome randomly in the range of 100-180.  The reason for this range is because the Alumina create reeds currently around 100 (ATCG's) in each reed.  I parsed each fasta file 3 times fowards and put each reed as a line in the toy_data.txt file.  I then reversed the data and cut the data from the back to make sure we got the end of the fasta files as well.  I did this 3 times.  Therefore for each fasta file we recieved I have iterated 6 times.  So, there is around 665000 reeds in the toy set.  This file is around 93 MB.  I am not sure yet if this will make our transriptome too good, but we will find out!  I can also make smaller or larger data as needed (given this compilation of data is kosher). 

Please let me know if you have any suggestions or concerns about the data.  I have not made the best documentation for the code to generate the data, but I have made it easy to manipulate it.


UPDATE (4/21):

I was thinking about the data created and I decided to delete 20 percent of the data randomly. Every 10 reads in the full toy_data file, I deleted 2 lines so we can potentially get a better idea of how the transcripton might act.  The pure toy_data file was ~665000 lines,  and now it is around 532000 lines.  Hopefully, this gives us a better idea for using parameters in a quicker way.  


UPDATE (4/26):

I made the reeds a fasta!!! Good luck!



Thank you!
-TJ

