#usr/bin/env python
#BIO-Genetics_Code_Genome_MN908947.3_gene_1 CORONA
#Developed By JohnMelodyMe

print("Corona Virus")
gene = open("sequence.txt","r")

#value to 0;
g=0;
a=0;
c=0;
t=0;


#Skip header:
gene.readline()
for line in gene:
    line = line.lower()
    for char in  line:
        if char == "g":
            g+=1
        if char == "a":
            a+=1
        if char == "c":
            c+=1
        if char == "t":
            t+=1
print("number of (g)'s" + str(g))
print("number of (a)'s" + str(a))
print("number of (c)'s" + str(c))
print("number of (t)'s" + str(t))

#0. = convert to floating
gc = (g+c+0.) / (a+t+c+g+0.)

print("gc content: " + str(gc))
detail = open("sequence.txt", "r")

detail.read()