## DNAGenre ##
This project is aimed at being free, used by organizations, and a startup project for study purposes. It is aimed at
making DNA analysis faster and more insightful (visionary).


## Dive Into ##
**About**

DNAGenre is a bioinformatics (study of DNA/RNA data using computers) oriented software that helps to read a DNA/RNA file and provide
insights in DNA/RNA data. This software is different in away that for the start, it is educational, free to use, and will
commonly be used in labs. The software logs in a user or signs up a user, then they can just select a real DNA/RNA file, and
the software will provide the insights of the DNA file. The problem the project solves is that it is educational and
helps learners know what is bioinformatics under the hood.

### Some Notes

**I.** `This project was 35% AI and 65% me.`

**II.** `This README has @2 and 2. @2 was in the old versions while 2 is the latest version.`

**III.** **Run only the `GUI.py` file to see the project in action.**

**IV.** **Check out the [website](https://sites.google.com/view/dnagenre/dnagenre-home) to get the executable (application) and more information.**

**Features**
1. Login and User Authentication.
2. Reading Folder for sequence files.
3. Using real bioinformatic files like **fastq**, **fasta**, (good with **txt** files in required format).
4. Bioinformatic analysis.
5. Codon Analysis.
6. Protein Analysis.
7. Simple Inbuilt Programming Language called `Decode`
8. User can delete a created account.
9. Show time or a progress bar on some processes.
10. Able to process an entire folder of DNA/RNA files.
11. User can compress DNA/RNA files that adhere to the guidelines using `MeloPress`
12. User can export data using the `Export` button.
13. Uses a simple algorithm to encrypt important files.


## Bugs Found ##
**DataTools.py**
``` python
def clean_data(filepath, label_char):
    """
    Receives a file path and separates strand labels from DNA
    Returns a dict of {strand labels: DNA}
    """
    DNAdict = dict()
    # Read Index, If No Read Index Then '?'
    label = '?'
    with open(filepath, 'r') as file:
        for i in file.readlines():
            i = i.strip()
            if label_char in str(i):
                label = i
                DNAdict[label] = ''
            else:
                DNAdict[label] = ''
                DNAdict[label] += i
    return DNAdict
```

**Note: This function has a bug and as we go on, we will see the bug.**

**1. Imagine A File Like This**
```
TTGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAGACGGCATCGATCGATCGA
GGGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAGACGGCATCGATCGATCGA
@1
ATGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAGACGGCATCGATCGATCGA
@2
GTGGCGTGAGTGCGGATCGATCGATGATCGATTCGATCGATCGCGCGAAAATAGAGCTAGCCC
@3
TCTTGATCGATCGATCGCTATTAGACGGCATGATCGATTCGATCGATCGCGCGAAAATATAGC
@4
ATCGTACCAGTACATACGATAGCCTCGTGATTCGATCGATGTGGCGTGAGTGCGGATCGATCG
@5
GTGGCAATATAGTGAGAGTAGAGTGCGGATCGAAATCGCTATCTAAGCTCAGTCGATTCTCTA
@6
CTAGACAGCTACAGTCCATGCGTGGCGTGAGCGATAGCTATCGATGACTCGATTGCGGATCGG
@7
GGTGAGTGCGGATCCGCTAGCTACCACATACGGGATAAAGCTAGTCTCTACGACGGTAGAGTA
@8
AGCTACGATTTATATCGGCTAGCCGTTATATAGCCGGACACAGATAGTACACAACAGTAGAGT
@9
GCTCGATAGAGTCCAGATCCATCAGACAGGGAATATATTACAGATACAGGGAGGTAGAGAAAC
@10
GTTACACAAGGATCGCTACAGATATCGGTACGCTAAATATCGCGCCTTAGTAGAGTCGAGTGT
```
When `clean_data` function is called, it makes label equal `?`. Now in this scenario, it finds DNA first but not label
hence label is set to `?` and DNA is collected. On the next run, the label is set to `?` but when we enter this line
`if label_char in str(i):` there is no `label_char` (for this scenario `label_char` is `@`) so it jumps to `else` and
else sets `label` to `''` (so our previous `?`:`'TTGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAGACGGCATCGATCGATCGA'` is
lost and now is `'?'`:`''` and the next line of code does add to the current dict key hence 
`'?'`:`'GGGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAGACGGCATCGATCGATCGA'`) and the code go on smoothly as intended.

**2. Imagine Another Like This**
```
TTGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAGACGGCATCGATCGATCGA
GGGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAGACGGCATCGATCGATCGA
@1ATGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAGACGGCATCGATCGATCGA
@2GTGGCGTGAGTGCGGATCGATCGATGATCGATTCGATCGATCGCGCGAAAATAGAGCTAGCCC
@3TCTTGATCGATCGATCGCTATTAGACGGCATGATCGATTCGATCGATCGCGCGAAAATATAGC
@4ATCGTACCAGTACATACGATAGCCTCGTGATTCGATCGATGTGGCGTGAGTGCGGATCGATCG
@5GTGGCAATATAGTGAGAGTAGAGTGCGGATCGAAATCGCTATCTAAGCTCAGTCGATTCTCTA
@6CTAGACAGCTACAGTCCATGCGTGGCGTGAGCGATAGCTATCGATGACTCGATTGCGGATCGG
@7GGTGAGTGCGGATCCGCTAGCTACCACATACGGGATAAAGCTAGTCTCTACGACGGTAGAGTA
@8AGCTACGATTTATATCGGCTAGCCGTTATATAGCCGGACACAGATAGTACACAACAGTAGAGT
@9GCTCGATAGAGTCCAGATCCATCAGACAGGGAATATATTACAGATACAGGGAGGTAGAGAAAC
@10GTTACACAAGGATCGCTACAGATATCGGTACGCTAAATATCGCGCCTTAGTAGAGTCGAGTGT
```
When `clean_data` function is run, it will function as explained earlier but when reaches this part
`@1ATGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAGACGGCATCGATCGATCGA` this code `if label_char in str(i):`runs, this 
creates the paradox of having keys equal to `@1ATGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAGACGGCATCGATCGATCGA` and 
values equal to `''` hence a result of `Read Index plus nucleotide chars`:`''` respectively.

**3. Imagine Another Third Last One Like This**
```
@1
ATGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAGACGGCATCGATCGATCGA

@2
GTGGCGTGAGTGCGGATCGATCGATGATCGATTCGATCGATCGCGCGAAAATAGAGCTAGCCC

@3
TCTTGATCGATCGATCGCTATTAGACGGCATGATCGATTCGATCGATCGCGCGAAAATATAGC

@4
ATCGTACCAGTACATACGATAGCCTCGTGATTCGATCGATGTGGCGTGAGTGCGGATCGATCG

@5
GTGGCAATATAGTGAGAGTAGAGTGCGGATCGAAATCGCTATCTAAGCTCAGTCGATTCTCTA

@6
CTAGACAGCTACAGTCCATGCGTGGCGTGAGCGATAGCTATCGATGACTCGATTGCGGATCGG

@7
GGTGAGTGCGGATCCGCTAGCTACCACATACGGGATAAAGCTAGTCTCTACGACGGTAGAGTA

@8
AGCTACGATTTATATCGGCTAGCCGTTATATAGCCGGACACAGATAGTACACAACAGTAGAGT

@9
GCTCGATAGAGTCCAGATCCATCAGACAGGGAATATATTACAGATACAGGGAGGTAGAGAAAC

@10
GTTACACAAGGATCGCTACAGATATCGGTACGCTAAATATCGCGCCTTAGTAGAGTCGAGTGT
```
When `clean_data` function is run, the label is always `?` if no label is met. On first iteration the label is set to `@1`
which is fine, on second iteration, we have our nucleotide characters so we set them as values for our `@1` label hence
`'@1'`:`'ATGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAGACGGCATCGATCGATCGA'` but here is a catch, on the third iteration,
we have a newline `\n` plus nothing `''` so this block is run `else:` hence setting the `'@1'` to the `stip()`ed
value (technically now is nothing `\n` = `''`) which leads to override hence this `key`:`''` on all iterations except 
the last part `@10`which the code will act normally since there are no `\n` plus `''` after the nucleotide characters.

**4. Imagine Another Second Last One Like This**
```
@1

ATGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAGACGGCATCGATCGATCGA
@2

GTGGCGTGAGTGCGGATCGATCGATGATCGATTCGATCGATCGCGCGAAAATAGAGCTAGCCC
@3

TCTTGATCGATCGATCGCTATTAGACGGCATGATCGATTCGATCGATCGCGCGAAAATATAGC
@4

ATCGTACCAGTACATACGATAGCCTCGTGATTCGATCGATGTGGCGTGAGTGCGGATCGATCG
@5

GTGGCAATATAGTGAGAGTAGAGTGCGGATCGAAATCGCTATCTAAGCTCAGTCGATTCTCTA
@6

CTAGACAGCTACAGTCCATGCGTGGCGTGAGCGATAGCTATCGATGACTCGATTGCGGATCGG
@7

GGTGAGTGCGGATCCGCTAGCTACCACATACGGGATAAAGCTAGTCTCTACGACGGTAGAGTA
@8

AGCTACGATTTATATCGGCTAGCCGTTATATAGCCGGACACAGATAGTACACAACAGTAGAGT
@9

GCTCGATAGAGTCCAGATCCATCAGACAGGGAATATATTACAGATACAGGGAGGTAGAGAAAC
@10

GTTACACAAGGATCGCTACAGATATCGGTACGCTAAATATCGCGCCTTAGTAGAGTCGAGTGT
```
When `clean_data` is run, you may expect that the situation above may happen but remember, on first iteration the label 
is `@1` and the values are set to be `''` (nothing) which maybe painful, but it has no pain this time since on next 
iteration, we have our nucleotide characters that will override the `''` (nothing) hence 
`'@1'`:`'ATGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAGACGGCATCGATCGATCGA'` and this goes on till the last iteration.

**5. Imagine Another Last One Like This**
```
@1
GACUACAGAUACCGAUCGAUAUACGACAGAUACAGAUAGACAGAUAGACAGAUCCUGACGAUCAGAUAGACAGAUAGACAGAUCCUGACGAUCUUA
UCAGCGAGCAUCUGAUCCUGAUAGCAUGCUGACGUAUGAGAAUUUAAUCGGUACGUACGUAGCUGCG
@2
UCAGCGAGCAUCUGAUCCUGAUAGCAUUUAAUCGGUACGUACGUAGCUGCGCGUAUUAUUACGAGAUAGACAGAUAGACAGAUCCUGACGAUCACG
UCAGCGAGCAUCUGAUCCUGAUAGCAUUUAAUCGGUAUUUAAUACAGAUCCUGACGAUUAAUACAGA
@3
AAAUGGAUAGUGAUGCUACGCUACGUAGCAUACGUUAUAUAUUACGUCGUAUGCUGACGUAUGAGAUAGACAGAUAGACAGAUCCUGACGAUCGUU
ACUACAGAUACCGAUCGAUAUAUCUGAUCCUGAUAGCAUUAUCUGAUCCUGAUAGCAUUAUUUAAUU
```
```python
def clean_data(filepath, label_char):
    """
    Receives a file path and separates strand labels from DNA
    Returns a dict of {strand labels: DNA}
    """
    DNAdict = dict()
    # Temporary Storage For Read Indexes
    label = '?'
    try:
        with open(filepath, 'r') as file:
            # Set 'File Pointer' To Start At Zero
            file.seek(0)
            for i in file.readlines():
                i = i.strip()
                if label_char in str(i):
                    label = i
                    DNAdict[label] = ''
                else:
                    DNAdict[label] = ''
                    DNAdict[label] += i
        return DNAdict
    # Any Exception Is An Error
    except Exception:
        return None
```
New updates so far like setting the `'File Pointer'` to zero (start) of file. When this `clean_data` function is run,
it reads in the file and starts the `for loop` looking for the `label_char`. In a scenario like ours above, it will find
the `label_char` on first iteration as `@1` then create a key for it having its value as `''` hence `'@1':''`. On second
iteration, it finds the nucleotide characters and then enters the `else` block so it sets again our `'@1':''` to `'@1':''`
and **sets(hear me loudly on this point, it sets not adds)** the current nucleotide characters. On third iteration, it
finds more nucleotide characters, it first checks is our `@1` in these nucleotide and **no** so it goes to our `else`
block which sets our `'@1':'GACUACAGAUACCGAUCGAUAUACGACAGAUACAGAUAGACAGAUAGACAGAUCCUGACGAUCAGAUAGACAGAUAGACAGAUCCUGACGAUCUUA
'` to `@1:''` and then adds the nucleotide characters to it hence `'@1':'UCAGCGAGCAUCUGAUCCUGAUAGCAUGCUGACGUAUGAGAAUUUAAUCGGUACGUACGUAGCUGCG
'`. In simple terms this line `DNAdict[label] = ''` in the `else` block makes our code 'forget' our last nucleotide
characters hence remembering the last bit of the nucleotide characters.
Hopefully you can figure out the bug now and how to navigate it before I can show you how I did it.

```
GACUACAGAUACCGAUCGAUAUACGACAGAUACAGAUAGACAGAUAGACAGAUCCUGACGAUCAGAUAGACAGAUAGACAGAUCCUGACGAUCUUA
UCAGCGAGCAUCUGAUCCUGAUAGCAUGCUGACGUAUGAGAAUUUAAUCGGUACGUACGUAGCUGCG
@2
UCAGCGAGCAUCUGAUCCUGAUAGCAUUUAAUCGGUACGUACGUAGCUGCGCGUAUUAUUACGAGAUAGACAGAUAGACAGAUCCUGACGAUCACG
UCAGCGAGCAUCUGAUCCUGAUAGCAUUUAAUCGGUAUUUAAUACAGAUCCUGACGAUUAAUACAGA
@3
AAAUGGAUAGUGAUGCUACGCUACGUAGCAUACGUUAUAUAUUACGUCGUAUGCUGACGUAUGAGAUAGACAGAUAGACAGAUCCUGACGAUCGUU
ACUACAGAUACCGAUCGAUAUAUCUGAUCCUGAUAGCAUUAUCUGAUCCUGAUAGCAUUAUUUAAUU
```
On such a file format, our function still works the same as above (remembering the last bit of the nucleotide characters)
but the first iteration is where I will shine light upon. So on first iteration, we do not have a label and so by default,
this `?` the label if `label` is not overridden. Our function enters `if` statement to check if our `i` (now nucleotide
characters) has our `label_char` hence **no** then `else` block is into play and for the first time makes `?` as `'?':''`
and adds nucleotide characters to it hence `'?':'GACUACAGAUACCGAUCGAUAUACGACAGAUACAGAUAGACAGAUAGACAGAUCCUGACGAUCAGAUAGACAGAUAGACAGAUCCUGACGAUCUUA
'` and on the next iteration it will forget the previous by setting again hence our `'?':'GACUACAGAUACCGAUCGAUAUACGACAGAUACAGAUAGACAGAUAGACAGAUCCUGACGAUCAGAUAGACAGAUAGACAGAUCCUGACGAUCUUA
'` becoming `'?':'UCAGCGAGCAUCUGAUCCUGAUAGCAUGCUGACGUAUGAGAAUUUAAUCGGUACGUACGUAGCUGCG
'`. This goes on and on till last iteration.

```
@1
GACUACAGAUACCGAUCGAUAUACGACAGAUACAGAUAGACAGAUAGACAGAUCCUGACGAUCAGAUAGACAGAUAGACAGAUCCUGACGAUCUUA
UCAGCGAGCAUCUGAUCCUGAUAGCAUGCUGACGUAUGAGAAUUUAAUCGGUACGUACGUAGCUGCG
@2
UCAGCGAGCAUCUGAUCCUGAUAGCAUUUAAUCGGUACGUACGUAGCUGCGCGUAUUAUUACGAGAUAGACAGAUAGACAGAUCCUGACGAUCACG
UCAGCGAGCAUCUGAUCCUGAUAGCAUUUAAUCGGUAUUUAAUACAGAUCCUGACGAUUAAUACAGA
@3
AAAUGGAUAGUGAUGCUACGCUACGUAGCAUACGUUAUAUAUUACGUCGUAUGCUGACGUAUGAGAUAGACAGAUAGACAGAUCCUGACGAUCGUU
ACUACAGAUACCGAUCGAUAUAUCUGAUCCUGAUAGCAUUAUCUGAUCCUGAUAGCAUUAUUUAAUU
@4
```
When Our function is run on this one, it runs normally but on the last part is where I will shine light upon. The second
last iteration, we have our `label` as `@4` and there are no nucleotide chars but there is a `\n` and `''`. Our function
uses Python's `strip()` function that removes `\n\t\r` and so much more hence we are left with `''` and this is set to
`@4` hence `'@4':''`.

Here is the revised code
```python
def clean_data(filepath, label_char):
    """
    Receives a file path and separates strand labels from DNA
    Returns a dict of {strand labels: DNA}
    """
    DNAdict = dict()
    # Temporary Storage For Read Indexes
    label = '?'
    try:
        with open(filepath, 'r') as file:
            # Set 'File Pointer' To Start At Zero
            file.seek(0)
            for i in file.readlines():
                i = i.strip()
                if label_char in str(i):
                    label = i
                    DNAdict[label] = ''
                else:
                    if label not in DNAdict.keys():
                        DNAdict[label] = ''
                    DNAdict[label] += i
        return DNAdict
    # Any Exception Is An Error
    except Exception:
        return None
```
In the `else` block, I added an `if` statement to check if the label is not in the `dict()` keys, if not then create it
one `key:value` (the key being '?' and value is whatever nucleotide characters we find) else jump the if statement. Also
added the `try` and `except` blocks so that any exception is an error.

**Note: Let me know if you have any better versions for this function.**

**user_home.py**

**The variables, functions or modules without declarations are handled in the class that is in the file**
```python
def start_DNA_analysis(self, filename):
    if validate_file(filename) == 0:
        DNA_label_entry = CTkEntry(self.user_home_window, placeholder_text="Enter DNA label",
                             font=("Menlo", 20), fg_color="black", text_color="green",
                             height=30, width=300, border_width=5, border_color="orange",
                             placeholder_text_color='cyan')
        DNA_label_entry.place(rely=0.915, relx=0.09)
        seq_type_entry = CTkEntry(self.user_home_window, placeholder_text="Enter DNA or RNA",
                                   font=("Menlo", 20), fg_color="black", text_color="green",
                                   height=30, width=300, border_width=5, border_color="orange",
                                   placeholder_text_color='cyan')
        seq_type_entry.place(rely=0.915, relx=0.45)
        submit_DNA_label_button = CTkButton(self.user_home_window, text="Submit", font=("Menlo", 25),
                                  text_color="blue", corner_radius=5, fg_color="black",
                                  command=lambda: DNA_analysis(filename, str(DNA_label_entry.get()),
                                  str(seq_type_entry.get()).upper(), self.user_home_window, self.username,
                                  self.firstname, self.lastname, User_Home))
        submit_DNA_label_button.place(rely=0.915, relx=0.8)
        return
    else:
        warning_2 = CTkLabel(self.user_home_window, text="File Problem", font=("Menlo", 30), fg_color="black",
                             text_color="red")
        warning_2.place(rely=0.87, relx=0.4)
        self.user_home_window.after(1000, warning_2.destroy)
        return
```
When you use the proper version, even some of the file formats that are forbidden (as shown above). This part of code
will run in order to get the read index (the text tagged on each sequence read) from the user.

**1. Imagine Something Like This**

After selecting a file to read and analyze, the widget for getting the read index (the text tagged on each sequence read)
pops up and asks the user for the read index (the text tagged on each sequence read). The user well instead of putting in
the most-common character in the read indexes (like for our scenario files, the most is `@`), the user puts in `@1` or
chooses `@` plus some of the other numbers (like `@2` and so on). Remember our function in `DataTools.py` that cleans
the file data.
That `clean_data` function will get the label we put (for instance `@1`). The function will look for only this (`@1`) and
add stuff (this time both the read indexes and the nucleotide characters because they are not the label) hence getting key
`read index (@1)`:`nucleotide characters` then `read index`:`next other read index` at respective intervals till read index
`@9` where it all happens, here at the nucleotide characters it gets `@1` and `@9`'s nucleotide chars hence
`'@1'`:`'GCTCGATAGAGTCCAGATCCATCAGACAGGGAATATATTACAGATACAGGGAGGTAGAGAAAC'`.
You may ask why it happened, well, remember that we store our data as strings (flexible, easy error checking and convenient)
and next read index has `@1` in it and the read index the user put was to find anything with `@1` in it and `@10` has `@1`
in it hence `@1`:`'GCTCGATAGAGTCCAGATCCATCAGACAGGGAATATATTACAGATACAGGGAGGTAGAGAAAC'` and then 
`@10`:`GTTACACAAGGATCGCTACAGATATCGGTACGCTAAATATCGCGCCTTAGTAGAGTCGAGTGT` because the code made a new key (because it had `@1`
in it) and gave it the next nucleotide characters `GTTACACAAGGATCGCTACAGATATCGGTACGCTAAATATCGCGCCTTAGTAGAGTCGAGTGT`

**2. Imagine The Next Scenario Like This**

A user puts in `@2` as the most-common read index. The first iteration, the loop finds `@1`, but `@1` doesn't have `@2`
in it so the code is makes it a `?` and then will add the next line of nucleotide characters. On second iteration, the loop
finds `@2` and it sets `@2` as key and adds the next line of nucleotide characters. As the iterations go on and overwrites
happen it will reach the last line of nucleotide characters hence adding that and ending the loop.

**hamming.py**

**1. Resources, If Statements and Logic**

Imagine I have a good valid file format like this
```
@1
GACUACAGAUACCGAUCGAUAUACGACAGAUACAGAUAGACAGAUAGACAGAUCCUGACGAUCAGAUAGACAGAUAGACAGAUCCUGACGAUCUUA
@2
UCAGCGAGCAUCUGAUCCUGAUAGCAUUUAAUCGGUACGUACGUAGCUGCGCGUAUUAUUACGAGAUAGACAGAUAGACAGAUCCUGACGAUCACG
@3
AAAUGGAUAGUGAUGCUACGCUACGUAGCAUACGUUAUAUAUUACGUCGUAUGCUGACGUAUGAGAUAGACAGAUAGACAGAUCCUGACGAUCGUU
```
Then a snippet of code in the massive code base like this
```python
    def show_hamming(self, DNA_data):

        """ Showing Hamming Distance """
        temp_seq_1 = str()
        temp_seq_2 = str()
        # Getting Sequences From Data
        for key, value in DNA_data.items():
            if key == str(self.seq_1_entry.get()):
                temp_seq_1 += str(value)
            elif key == (self.seq_2_entry.get()):
                temp_seq_2 += str(value)
```
A briefing on If Statements, If statements are clauses in code that check conditions, whether `True` or `False`. In a
scenario above, the if statement starts in the loop and let's say maybe user entered `@1` as read index 1 and `@1` as
read index 2 for `Hamming Distance` (Hamming distance checks index by index for not matching nucleotides while respecting
the index, if I am checking index 1 of seq 1 then I must check index 1 of seq 2 too), it checks (is `key` == `@1` and yes)
so it sets `temp_seq_1` to the nucleotide characters for `@1` and the if statement breaks out (like it doesn't check again)
so we leave the iteration with `@1` and go to the next iterations that have other keys (not `@1`) hence if seq 2 is `@1`.
The shot of `@2` is lost.

![Screenshot 2025-08-10 at 09.07.03.png](addons/Screenshot%202025-08-10%20at%2009.07.03.png)

But on code like this

```python
    def show_hamming(self, DNA_data):

        """ Showing Hamming Distance """
        temp_seq_1 = str()
        temp_seq_2 = str()
        # Getting Sequences From Data
        for key, value in DNA_data.items():
            if key == str(self.seq_1_entry.get()):
                temp_seq_1 += str(value)
            if key == (self.seq_2_entry.get()):
                temp_seq_2 += str(value)
```
The two If statements run because all are 'primary' (they must run since they start the 'check conditions system')
hence no errors.

![Screenshot 2025-08-10 at 09.11.43.png](addons/Screenshot%202025-08-10%20at%2009.11.43.png)

Notes:

**I.** **If You really love scenario 1 and it is useful to you, scenario 1 uses less computer resources. If you love
scenario 2, it will take more time on big data. It is known that a sequence compared to itself is a photocopy and I love
optimization hence I left scenario 1 as default. Let me know which is best.**


**II.** When entering a Read Index to start hamming, just enter a number (like `1` or `2`) this is used as a reference
that the user wants sequence at read index number `1` or read index number `2`. Do not use `@1` or `@2` depending on what
read index you want, just use `1` or `2` or whatever read index you want but without other characters (in this case those
characters are `@` just type in a number). This is because I just realized that dictionaries do not allow duplicate keys
but allow duplicate values. Imagine user file has duplicate keys for read index hence wrong data generated. I have decided
to use numbers because numbers never repeat as a **counter** counts on.

**requirements_2.py** and **ProteinSite.py**

**1. Invalid Data For Read Indexes**
```
@1
ATCGTGTCGATCATCTAGCTACACGATACAGGCATATCGATCCATGCTTAGCTAGCACAGACT
@2
CGGCATAGCGATGTTGGACACGATTTTAAGAGATATATATAGCTAGCTACTTCGATGTACACA
@3
TAGCTACACTAGCACAGACTTGGACACGATTTTAAGAGATATATATAGTAGCTACAATCGTAG
@4
TCGTAGCTAGGACGCGCATATATACAAGAAGTAACAAATAATATCGATAATCGACGCGTATTT
@5
GGGAAGAATTACAGGATACTTGGACACCGCATATAATTAGCTAGGATTTCTTGGACACGGCTA
@6
ACTTGGCCGTAAAACGACGCATATAATCGCATCGCGTTTACTTGGACCGCGTAAAAACGATTT
@7
CCGCGTATATATAATCGCGTAGGACACGAGCGTAGAGATCCCAACACGGGTTAATAGAAAAAG
@8
AAGAGATTGGGTTAAAGATCGATCTAGGAATAGCTAAATGCTAGATAAATACACACTTGGACA
@9
ACTTGGACCGCGTAAATATATGCAAGAGATCGCGGAATCTAACTTGGCGCGCTTAGTATTTAG
@10
CCTTGGACACGACTTGGACAGAATTCGATGATAGATAGACCACAGAATAGATCACCGCGCGCG
@11
@12
@13
```

When time comes for showing proteins, the `self.draw_proteins(self, proteins_data)` function in `ProteinSite.py` and the
`self.show_proteins(self)` function in `requirements.py` look for a Read Index and its data. If the algorithm does not find
data for that current Read Index or the data cannot make a protein, then it marks it as `Has Invalid Data`.

Below is a Read Index `1` that had valid DNA data to make proteins--even though it has no proteins.

![Screenshot 2026-08-11 at 15.21.20.png](addons/Screenshot%202026-08-11%20at%2015.21.20.png)

Below is a Read Index `13` that had invalid DNA data to make proteins.

![Screenshot 2026-08-11 at 15.21.32.png](addons/Screenshot%202026-08-11%20at%2015.21.32.png)

Note: Above is DNA with respect to `SeqType`.

**DNAsite.py**

**1. The Issue Of Read Index Embedded In The Data**

```
@1
ATCGTGTCGATCATCTAGCTACACGATACAGGCATATCGATCCATGCTTAGCTAGCACAGACT
@2
CGGCATAGCGATGTTGGACACGATTTTAAGAGATATATATAGCTAGCTACTTCGATGTACACA
@3
TAGCTACACTAGCACAGACTTGGACACGATTTTAAGAGATATATATAGTAGCTACAATCGTAG
@4
TCGTAGCTAGGACGCGCATATATACAAGAAGTAACAAATAATATCGATAATCGACGCGTATTT
@5
GGGAAGAATTACAGGATACTTGGACACCGCATATAATTAGCTAGGATTTCTTGGACACGGCTA
@6
ACTTGGCCGTAAAACGACGCATATAATCGCATCGCGTTTACTTGGACCGCGTAAAAACGATTT
@7
CCGCGTATATATAATCGCGTAGGACACGAGCGTAGAGATCCCAACACGGGTTAATAGAAAAAG
@8
AAGAGATTGGGTTAAAGATCGATCTAGGAATAGCTAAATGCTAGATAAATACACACTTGGACA
@9
ACTTGGACCGCGTAAATATATGCAAGAGATCGCGGAATCTAACTTGGCGCGCTTAGTATTTAG
@10
CCTTGGACACGACTTGGACAGAATTCGATGATAGATAGACCACAGAATAGATCACCGCGCGCG
@11
@12
SHOPXMZMZJJHGGHJIIIIKKRKKEKKEKRKRKJJKJKKLKLLMP::""(!*@(*!(!@*88
```

or

```
@1
ATCGTGTCGATCATCTAGCTACACGATACAGGCATATCGATCCATGCTTAGCTAGCACAGACT
@2
CGGCATAGCGATGTTGGACACGATTTTAAGAGATATATATAGCTAGCTACTTCGATGTACACA
@3
TAGCTACACTAGCACAGACTTGGACACGATTTTAAGAGATATATATAGTAGCTACAATCGTAG
@4
TCGTAGCTAGGACGCGCATATATACAAGAAGTAACAAATAATATCGATAATCGACGCGTATTT
@5
GGGAAGAATTACAGGATACTTGGACACCGCATATAATTAGCTAGGATTTCTTGGACACGGCTA
@6
ACTTGGCCGTAAAACGACGCATATAATCGCATCGCGTTTACTTGGACCGCGTAAAAACGATTT
@7
CCGCGTATATATAATCGCGTAGGACACGAGCGTAGAGATCCCAACACGGGTTAATAGAAAAAG
@8
AAGAGATTGGGTTAAAGATCGATCTAGGAATAGCTAAATGCTAGATAAATACACACTTGGACA
@9
ACTTGGACCGCGTAAATATATGCAAGAGATCGCGGAATCTAACTTGGCGCGCTTAGTATTTAG
@10
CCTTGGACACGACTTGGACAGAATTCGATGATAGATAGACCACAGAATAGATCACCG@GCGCG
```

Since the entered `Read Index` value that is entered below--in this case is `@`

![Screenshot 2025-08-05 at 11.26.39.png](addons/Screenshot%202025-08-05%20at%2011.26.39.png)

is embedded in the last data
`SHOPXMZMZJJHGGHJIIIIKKRKKEKKEKRKRKJJKJKKLKLLMP::""(!*@(*!(!@*88` or `CCTTGGACACGACTTGGACAGAATTCGATGATAGATAGACCACAGAATAGATCACCG@GCGCG
`,that data is not considered as
data but rather as a Read index since it has `@` in it. Its value (data) now becomes an empty string.

**Here is output from my investigation.**

{\
 '@1': 'ATCGTGTCGATCATCTAGCTACACGATACAGGCATATCGATCCATGCTTAGCTAGCACAGACT',\
 '@2': 'CGGCATAGCGATGTTGGACACGATTTTAAGAGATATATATAGCTAGCTACTTCGATGTACACA',\
 '@3': 'TAGCTACACTAGCACAGACTTGGACACGATTTTAAGAGATATATATAGTAGCTACAATCGTAG',\
 '@4': 'TCGTAGCTAGGACGCGCATATATACAAGAAGTAACAAATAATATCGATAATCGACGCGTATTT',\
 '@5': 'GGGAAGAATTACAGGATACTTGGACACCGCATATAATTAGCTAGGATTTCTTGGACACGGCTA',\
 '@6': 'ACTTGGCCGTAAAACGACGCATATAATCGCATCGCGTTTACTTGGACCGCGTAAAAACGATTT',\
 '@7': 'CCGCGTATATATAATCGCGTAGGACACGAGCGTAGAGATCCCAACACGGGTTAATAGAAAAAG',\
 '@8': 'AAGAGATTGGGTTAAAGATCGATCTAGGAATAGCTAAATGCTAGATAAATACACACTTGGACA',\
 '@9': 'ACTTGGACCGCGTAAATATATGCAAGAGATCGCGGAATCTAACTTGGCGCGCTTAGTATTTAG',\
 '@10': 'CCTTGGACACGACTTGGACAGAATTCGATGATAGATAGACCACAGAATAGATCACCGCGCGCG',\
 '@11': '',\
 '@12': '',\
 'SHOPXMZMZJJHGGHJIIIIKKRKKEKKEKRKRKJJKJKKLKLLMP::""(!*@(\*!(!@*88': ''\
}\
\
or

{\
 '@1': 'ATCGTGTCGATCATCTAGCTACACGATACAGGCATATCGATCCATGCTTAGCTAGCACAGACT',\
 '@2': 'CGGCATAGCGATGTTGGACACGATTTTAAGAGATATATATAGCTAGCTACTTCGATGTACACA',\
 '@3': 'TAGCTACACTAGCACAGACTTGGACACGATTTTAAGAGATATATATAGTAGCTACAATCGTAG',\
 '@4': 'TCGTAGCTAGGACGCGCATATATACAAGAAGTAACAAATAATATCGATAATCGACGCGTATTT',\
 '@5': 'GGGAAGAATTACAGGATACTTGGACACCGCATATAATTAGCTAGGATTTCTTGGACACGGCTA',\
 '@6': 'ACTTGGCCGTAAAACGACGCATATAATCGCATCGCGTTTACTTGGACCGCGTAAAAACGATTT',\
 '@7': 'CCGCGTATATATAATCGCGTAGGACACGAGCGTAGAGATCCCAACACGGGTTAATAGAAAAAG',\
 '@8': 'AAGAGATTGGGTTAAAGATCGATCTAGGAATAGCTAAATGCTAGATAAATACACACTTGGACA',\
 '@9': 'ACTTGGACCGCGTAAATATATGCAAGAGATCGCGGAATCTAACTTGGCGCGCTTAGTATTTAG',\
 '@10': '',\
 'CCTTGGACACGACTTGGACAGAATTCGATGATAGATAGACCACAGAATAGATCACCG@GCGCG': ''\
}


## Usage ##
`Big Note`

    In computers, counting starts at 0 (zero) but to simplify this for you I have added 1 (one)
    to the GUI Display but left it as 0 (zero) in the computer processes so that you can see
    that as usual we count from 1 (one) yet relative to the computer, it started at 0 (zero) but
    relative to you, it starts at 1 (one).
    
    Hence; If you want the first position of anything, just use 1 (one) in the GUI

    So use the numeracy on the screen and do not assume!

**1. File Format**
```
@1
ATGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAGACGGCATCGATCGATCGA
@2
GTGGCGTGAGTGCGGATCGATCGATGATCGATTCGATCGATCGCGCGAAAATAGAGCTAGCCC
@3
TCTTGATCGATCGATCGCTATTAGACGGCATGATCGATTCGATCGATCGCGCGAAAATATAGC
@4
ATCGTACCAGTACATACGATAGCCTCGTGATTCGATCGATGTGGCGTGAGTGCGGATCGATCG
@5
GTGGCAATATAGTGAGAGTAGAGTGCGGATCGAAATCGCTATCTAAGCTCAGTCGATTCTCTA
@6
CTAGACAGCTACAGTCCATGCGTGGCGTGAGCGATAGCTATCGATGACTCGATTGCGGATCGG
@7
GGTGAGTGCGGATCCGCTAGCTACCACATACGGGATAAAGCTAGTCTCTACGACGGTAGAGTA
@8
AGCTACGATTTATATCGGCTAGCCGTTATATAGCCGGACACAGATAGTACACAACAGTAGAGT
@9
GCTCGATAGAGTCCAGATCCATCAGACAGGGAATATATTACAGATACAGGGAGGTAGAGAAAC
@10
GTTACACAAGGATCGCTACAGATATCGGTACGCTAAATATCGCGCCTTAGTAGAGTCGAGTGT
```
OR
```
@1
GACUACAGAUACCGAUCGAUAUACGACAGAUACAGAUAGACAGAUAGACAGAUCCUGACGAUCAGAUAGACAGAUAGACAGAUCCUGACGAUCUUA
UCAGCGAGCAUCUGAUCCUGAUAGCAUGCUGACGUAUGAGAAUUUAAUCGGUACGUACGUAGCUGCG
@2
UCAGCGAGCAUCUGAUCCUGAUAGCAUUUAAUCGGUACGUACGUAGCUGCGCGUAUUAUUACGAGAUAGACAGAUAGACAGAUCCUGACGAUCACG
UCAGCGAGCAUCUGAUCCUGAUAGCAUUUAAUCGGUAUUUAAUACAGAUCCUGACGAUUAAUACAGA
@3
AAAUGGAUAGUGAUGCUACGCUACGUAGCAUACGUUAUAUAUUACGUCGUAUGCUGACGUAUGAGAUAGACAGAUAGACAGAUCCUGACGAUCGUU
ACUACAGAUACCGAUCGAUAUAUCUGAUCCUGAUAGCAUUAUCUGAUCCUGAUAGCAUUAUUUAAUU
```
File Formats are key for good results, so I recommend a file with this format `fastq`,`fasta` or a `txt` file with this 
format for nice and clean results and not to encounter some of the bugs that are in the `Bugs Found` section.

**2. Sign Up Tutorial**

![Screenshot 2025-08-16 at 19.11.04.png](addons/Screenshot%202025-08-16%20at%2019.11.04.png)
When signing up, avoid commas because I used them for separating data in the database. What happens in most cases is that
when they are passed, they hinder the healthy retrieval of data from the database hence causing injections, data breaches
and so much database problems. I have put good measures to prevent this by not allowing commas from users.

**Note: If you are a security expert or have a better way, please reach out to me via the contacts in the contacts section.**

**3. File Creation and File Reading tutorial**

![Screenshot 2025-08-16 at 19.19.29.png](addons/Screenshot%202025-08-16%20at%2019.19.29.png)
**I.** When entering a folder name to create, by default I have redirected the folder creation to the `Desktop`. All created
folder names without a full path (absolute file path) to where to create them will be put in the Desktop. If there is an
absolute file path, that is where the folder creation will happen.

When reading a folder, it is encouraged to enter the absolute folder path to where the folder is hence reading it healthily.
If you do not provide an absolute folder path, the program with error at you.

**II.** If user (you) ever needs to see the full file name if it could work respective of your file length after the
folder name is discarded, use this trick.

Below is a scenario whereby if the folder name is discarded the filename that remains is less than or equal to 25 characters.

![Screenshot 2026-08-22 at 14.57.24.png](addons/Screenshot%202026-08-22%20at%2014.57.24.png)

When entering the folder to display its contents and user (you) do this, that is why the folder content is displayed like this.

![Screenshot 2026-08-22 at 14.57.41.png](addons/Screenshot%202026-08-22%20at%2014.57.41.png)

Add `/` for Mac or `\\` for Windows to achieve the result below.

![Screenshot 2026-08-22 at 14.58.12.png](addons/Screenshot%202026-08-22%20at%2014.58.12.png)

**4. Is It A DNA File, RNA File OR Not**

![Screenshot 2025-08-16 at 19.44.22.png](addons/Screenshot%202025-08-16%20at%2019.44.22.png)
I have simple function that reads in a file pressed and counts the `A, T, G, T, U`. If those letters are greater than the
other stuff in the file, then the file would be valid to be analyzed.

**Note: But file validation is not yet over.**

**5. Read Index Usage**

![Screenshot 2025-08-05 at 11.26.39.png](addons/Screenshot%202025-08-05%20at%2011.26.39.png)
When entering the `Read Index`, please enter a character that is most-common in all the read indexes for better and
reasonable results.
![Screenshot 2025-08-05 at 11.26.39.png](addons/Screenshot%202025-08-05%20at%2011.26.39.png)
This is where part two of file validation occurs, when you enter the file, it will also ask you to enter a sequence type
either it is `DNA` or `RNA`. If all do not match what it has from the file then you cannot proceed to analysis.

**Note:**\
In case user (your) enters the `Read Index`. I use a **Python Dictionary** that does not allow duplicate
keys but allows duplicate values. Having two or more `Read Indexes` that are literal duplicates--which are treated as
keys--causes the **Python Dictionary** to naturally consider that last duplicate. To avoid this, always avoid using duplicate `Read Indexes`

**6. Codon Usage Entry**

![Screenshot 2025-08-16 at 20.01.55.png](addons/Screenshot%202025-08-16%20at%2020.01.55.png)
When entering a Read Index to get the codon activity, just enter a number (like `1` or `2`) this is used as a reference
that the user wants codons in read index number `1` or read index number `2`. Do not use `@1` or `@2` depending on what
read index you want, just use `1` or `2` or whatever read index you want but without other characters (in this case those
characters are `@` just type in a number). This is because I just realized that dictionaries do not allow duplicate keys
but allow duplicate values. Imagine user file has duplicate keys for read index hence data generated for last Read Index--since
it is the last duplicate and Python Dictionaries will consider the last duplicate due to overwriting previous Read Indexes
and their data till the last Read Index has nothing to overwrite it. I have decided to use numbers because numbers never
repeat as a **counter** counts on.

**Note:**

    1+ means that is a normal read of that sequence

    1- means that is a reversed complement read of that sequence

**7. Protein Interpretation**

![Screenshot 2025-08-06 at 08.18.01.png](addons/Screenshot%202025-08-06%20at%2008.18.01.png)

Display of Proteins would look messy if I displayed proteins by finding the instance of `M` (start Codon) without seeing
that there are proteins inside of proteins. For instance as in the picture, a long protein is shown but not till its `_`
(stop Codon). Since the code has this `if letter_6 == "M":`, it will cut proteins short hence not seeing the full picture.

![Screenshot 2025-08-06 at 08.18.28.png](addons/Screenshot%202025-08-06%20at%2008.18.28.png)

Since I knew this was a string (it is NOT a list), I added this line of code 
`if letter_6 == "M" and proteins[i_6 - 1] == '\'':`. The long protein has a protein subunit but with the new code inserted,
the long protein is shown and the next "protein(s)" is a protein subunit(s) of the long protein above it.

Hence
![Screenshot 2025-08-07 at 09.35.33.png](addons/Screenshot%202025-08-07%20at%2009.35.33.png)

**Note: Once again** 

    1+ means that is a normal read of that sequence

    1- means that is a reversed complement read of that sequence



**Note:** My proteinsynthesis function shows protein(s) from **open reading frames**.

![Screenshot 2026-07-26 at 16.13.34.png](addons/Screenshot%202026-07-26%20at%2016.13.34.png)

**Note:**\
When entering a Read Index to get the protein(s), just enter a number (like `1` or `2`) this is used as a reference
that the user wants protein(s) in read index number `1` or read index number `2`. Do not use `@1` or `@2` depending on what
read index you want, just use `1` or `2` or whatever read index you want but without other characters (in this case those
characters are `@` just type in a number). This is because I just realized that dictionaries do not allow duplicate keys
but allow duplicate values. Imagine user file has duplicate keys for read index hence wrong data generated. I have decided
to use numbers because numbers never repeat as a **counter** counts on.

**8. Proteinsynthesis Time Calculation**

![Screenshot 2025-08-07 at 11.10.50.png](addons/Screenshot%202025-08-07%20at%2011.10.50.png)

My timer can be off by some amount of time because of factors like laptop updating time late due to it finishing other
tasks and mostly due to using python threads which can be interrupted by python's Global Interpreter Lock (GIL). The GIL
allows one thread to execute at a time which boosts the interpreter's speed but giving up true parallelism of processes.

**Note: For just keeping track of time and proteinsynthesis, I decided to use threads (easy to understand).**

**9. Hamming Distance**

![Screenshot 2025-08-16 at 20.58.31.png](addons/Screenshot%202025-08-16%20at%2020.58.31.png)
When entering the read index, enter the actual read index (for our scenario, the read index would be `@1`) depending on
which indexes you want to "ham".

    Note: LengthOfEach - is the length of the current view and its analysis | is the entire 
                         length of each of the strands

**10. K-mer By Search**

![Screenshot 2025-08-16 at 21.22.00.png](addons/Screenshot%202025-08-16%20at%2021.22.00.png)
As you can see, enter the `Read Index` as shown on the left of the screen, enter the `K-mer` to be found as shown on the right
then press `Search`. Once search is pressed, the `k-mer Count` will be updated and the indexes where the `K-mer` is found will
be found will be shown.

`K-mer Count` - This is the number of times the k-mer appeared

**App Hack:**

    You can see how many nucleotides are there in the "Read Index" by entering the 
    nucleotide base (like "A" in order to get how many "A" are there)

![Screenshot 2025-08-16 at 21.57.00.png](addons/Screenshot%202025-08-16%20at%2021.57.00.png)

**Note: The numbers shown in the visualization panel are the index where the `K-mer` starts then add the `K-mer`'s length**
**(the `K-mer`'s position inclusive - if the `K-mer` length is 5, then just add 5 to the index and **subtract 1** hence you
get the stop position) forward and that is where the `K-mer` stops.**

**11. K-mer By Length**

![Screenshot 2025-08-16 at 22.39.39.png](addons/Screenshot%202025-08-16%20at%2022.39.39.png)
Enter the Read Index as shown on the left of the screen and enter a valid k-mer length on the right of the screen. When
`Search` is pressed, it looks for all two-longed k-mer and gives you a visualization of k-mer by length.

`Appearance(s)` - This is the number of times a two-longed k-mer or n-longed k_mer was found.

`Length` - Length of the sequence.

**App Hack:**

    You can see the nucleotide count for a Read Index by just asking the program for all
    single-longed nucleotides characters hence getting all nucleotides and their count

![Screenshot 2025-08-17 at 07.24.54.png](addons/Screenshot%202025-08-17%20at%2007.24.54.png)

**12. Decode**

Decode is a primitive programming language that will help users (you) complete more custom tasks that are not premade in the
app. In this case it has just features like `setting variables` `comments` mathematical operations like
`addition` `subtraction` `division` `multiplication` and `loops` `logcial statements` `printr`. All of these can help a user
get a simple task done like `GC Content` `Nucleotide Count` `AT Content` `Some Mathematical Algorithms`.

**Cannot Handle Decimals**

Let's say user starts by setting 5.4 to a variable called x then sets 0.0 to a variable y that will later store our result.
When user tries to divide the value in x by 3.2, Decode will error saying that 3.2 is not an integer.

![Screenshot 2026-01-12 at 17.42.18.png](addons/Screenshot%202026-01-12%20at%2017.42.18.png)

REASON: Every variable receives a string version of the value user gives it. When you set 5.4 to x, Decode thinks it is
string version of 5.4 which is 5.4 into x hence no error. When user divides x by 3.2, Decode recognizes that these are not
integers and errors saying `not_integer`

\
Let's say user sets a variable called x which we will be our result variable and set it to 0. Later user tries to divide
3 by 2 which will result into a decimal. Decode uses integer division in division (quotients are stripped of their
decimal part and made integers by leaving the floor - the whole number like 3 divided by 2 is 1.5 but the .5 is removed
and the 1 is left as the answer)

![Screenshot 2026-01-12 at 18.08.13.png](addons/Screenshot%202026-01-12%20at%2018.08.13.png)

REASON: Decode first checks if the divisor and the dividend are integers and proceeds and uses integer division

**Cannot Handle Nested Loops**

Let's say user sets two loops, one outside and one inside the other forming nested loops.

![Screenshot 2026-01-12 at 18.54.18.png](addons/Screenshot%202026-01-12%20at%2018.54.18.png)

When `when` is called, its program counter or location is stored and used as a reference to start from next time the loop
needs to start again if condition is not met. In this scenario the first `when` location is saved and the loop goes on but
another `when` is encountered which overwrites the previous `when` saved location. Since this current `when` is the one
remembered, its loop in run and when finished, the program breaks out and continues. When the outer loop's `end` is found,
the other loop that ran overwrote or reset important variables needed for this `end` to execute hence this `end` is skipped
and program continues without errors. The program does not run as intended since one loop can run at a time NOT loop
inside a loop.

**Solution**\
This code is supposed to subtract from `d` 10 times while adding 1 to `e` but during each iteration of this--what I have
just explained--it counts down from 5 to 0. Using `when` loops cannot cut this but using `branch` can get the job done. With
a new feature called a **label** (is a marker in code) plus **code indexing** (using the index of a line of code as a 'jump to')
user (you) can jump around in code, produce loops, and sophisticated
programs.

![Screenshot 2026-08-12 at 23.38.29.png](addons/Screenshot%202026-08-12%20at%2023.38.29.png)

**Full Code**
```
set d 10
set e 0

label_1:
set f 5

label_2:
sub f f 1
if f 0
branch 14
done

branch label_2
sub d d 1
add e e 1

if d 0
stop
done

branch label_1
```


**Cannot Handle Nested If Statements Logically**

If statements have many twists and turns. In this scenario user sets up an if statement inside an if statement. An if
statement does not need to save anything so no worry at the `if k 1` part but when Decode reaches `done` it checks if the
program is running, if it is then `done` is skipped. If the program is NOT running, `done` will release the program from
not running to running and if there is code following then that code will always be run.

![Screenshot 2026-01-12 at 20.35.40.png](addons/Screenshot%202026-01-12%20at%2020.35.40.png)

**Solution**

Below is the usage of `branch` which is demonstrating its versatility in `Nested Loop Crisis` to `Nested If Statements Crisis`.
It makes the code easier to follow, debug, and predictable.

**Note: Technically this is a nested if statement.**

![Screenshot 2026-08-12 at 23.51.59.png](addons/Screenshot%202026-08-12%20at%2023.51.59.png)


**Infinite Loops**

In `when d` Decode is checking if `d` is zero and if not, then the program will run forever or indefinitely. The app will
stop responding and the program will go on. Threading is a useful library that allows running more than one process at the
same time. I made the RUN button start the "child" thread that runs the code while the "main" thread runs the GUI interface.
I added a STOP button that ends the "child" thread hence the GUI interface runs normally and the code is run normally at
the same time.

![Screenshot 2026-01-12 at 20.40.16.png](addons/Screenshot%202026-01-12%20at%2020.40.16.png)


**Using `Branch` Is Powerful But Tricky**

```
@1
TTTTTTGGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAG
@2
GTGGCGTGAGTGCGGATCGATCGATGATCGATTCGATCGATCGCGCGAAA
@3
TCTTGATCGATCGATCGCTATTAGACGGCATGATCGATTCGATCGATCGC
@4
ATCGTACCAGTACATACGATAGCCTCGTGATTCGATCGATGTGGCGTGAG
@5
GTGGCAATATAGTGAGAGTAGAGTGCGGATCGAAATCGCTATCTAAGCTC
@6
CTAGACAGCTACAGTCCATGCGTGGCGTGAGCGATAGCTATCGATGACTC
@7
GGTGAGTGCGGATCCGCTAGCTACCACATACGGGATAAAGCTAGTCTCTA
@8
AGCTACGATTTATATCGGCTAGCCGTTATATAGCCGGACACAGATAGTAC
@9
GCTCGATAGAGTCCAGATCCATCAGACAGGGAATATATTACAGATACAGG
@10
GTTACACAAGGATCGCTACAGATATCGGTACGCTAAATATCGCGCCTTAG
@11
ACGGCATCGATCGATAGAGCTAGCCCGCGAAAATATAGCTGCGGATCGAT
@12
AGTCGATTCTCTAGATTGCGGATCGGCGACGGTAGAGTAACAACAGTAGA
@13
GAGGTAGAGAAACTAGAGTCGAGTGTCGGTCCGTTATATAGCATCAGACA
@14
GGGGTGAGTGAGTGCGGATCGACGATAGCCTCGGGCAATATAGTTAACCA
@15
GAGTGCGGATCGAGGTGAGTGAGTGCAATATAGTTAACCATAGTTAACCA
@16
GCTAGCCGTTATATAGCCGTCGCTACAGATATGGATCGACGAGAGTGCAG
@17
CGGATTTATATCGGCTAGCCGAGATTTATATCGGCTAGCCCCGGTACGAC
@18
GAGTGAGTGCGGATCGAGGTGAGTGAGTGCAGGATCGAGGTGAGTGAGTG
@19
CACCGCTAGCTCCGCCTCGGGCAATATAGTATAGCCTCGGGCAATATAGT
@20
GTTACACAAGTACATACGATAGCCTCGTACGATAGCCTCGTGTAGCCCGG
@21
TTTTTTGGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAG
@22
GTGGCGTGAGTGCGGATCGATCGATGATCGATTCGATCGATCGCGCGAAA
@23
TCTTGATCGATCGATCGCTATTAGACGGCATGATCGATTCGATCGATCGC
@24
ATCGTACCAGTACATACGATAGCCTCGTGATTCGATCGATGTGGCGTGAG
@25
GTGGCAATATAGTGAGAGTAGAGTGCGGATCGAAATCGCTATCTAAGCTC
@26
CTAGACAGCTACAGTCCATGCGTGGCGTGAGCGATAGCTATCGATGACTC
@27
GGTGAGTGCGGATCCGCTAGCTACCACATACGGGATAAAGCTAGTCTCTA
@28
AGCTACGATTTATATCGGCTAGCCGTTATATAGCCGGACACAGATAGTAC
@29
GCTCGATAGAGTCCAGATCCATCAGACAGGGAATATATTACAGATACAGG
@30
GTTACACAAGGATCGCTACAGATATCGGTACGCTAAATATCGCGCCTTAG
@31
ACGGCATCGATCGATAGAGCTAGCCCGCGAAAATATAGCTGCGGATCGAT
@32
AGTCGATTCTCTAGATTGCGGATCGGCGACGGTAGAGTAACAACAGTAGA
@33
GAGGTAGAGAAACTAGAGTCGAGTACGATAGCCTCGGATAGCCTCGAGTG
@34
GGGGTGAGTGAGTGCGGATCGACGATAGCCTCGGGCAATATAGTTAACCA
@35
GAGTGCGGATCGAGGTGAGTGAGTGCAATATAGTTAACCATAGTTAACCA
@36
GCTAGCCGTTATATAGCCGTCGCTACAGATATGGATCGAAGCCTCGGTCA
@37
CGGATTTATATCAGCCTCGATATCGGCTAGCCCCGGTACGACAGCCTCGA
@38
CAGGATTGCGGATCGAGGTGAGTGAGTGCAGGATCGAGGTGAAGTGAGTG
@39
CACCGCTAGCTCCGAGCCTCGCTCGGGCAATATAGCCTCGCCAGCCTCAG
@40
TAAAAGCCTCGACATACGATAGCCTCGTACGATAGCCTCGTGTAGCCCGG
@41
TTTTTTGGGCGTGAGTGCGGATCGATCGATGATCGATCGATCGCTATTAG
@42
GTGGCGTGAGTGCGGATCGATCGATGATCGATTCGATCGATCGCGCGAAA
@43
TCTTGATCGATCGATCGCTATTAGACGGCATGATCGATTCGATCGATCGC
@44
ATCGTACCAGTACATACGATAGCCTCGTGATTCGATCGATGTGGCGTGAG
@45
GTGGCAATATAGTGAGAGTAGAGTGCGGATCGAAATCGCTATCTAAGCTC
@46
CTAGACAGCTACAGTCCATGCGTGGCGTGAGCGATAGCTATCGATGACTC
@47
GGTGAGTGCGGATCCGCTAGCTACCACATACGGGATAAAGCTAGTCTCTA
@48
AGCTACGATTTATATCGGCTAGCCGTTATATAGCCGGACACAGATAGTAC
@49
GCTCGATAGAGTCCAGATCCATCAGACAGGGAATATATTACAGATACAGG
@50
CAGGATAAGGATCGCTACAGATATCGGTACGCTAAATATCGCGCCTTAGT
```

Using `branch` is a very crucial decision when writing readable and viable code but can be a pain too if not
used appropriately. Let's try code that is using `branch` inappropriately (Bad code) and code that is using `branch`
appropriately (Good code).

**Good code**\
`set x a`\
`// AT counter`\
`set y 0`

`label_1:`

`if - A`\
`branch 22`\
`done`

`sub x x 1`\
`add c c 1`

`if c a`\
`stop`\
`done`

`if x 0`\
`stop`\
`done`\
`branch label_1`

`if c a`\
`stop`\
`done`

`printr 1`\
`add c c 1`

`if c a`\
`stop`\
`done`

`if - T`\
`printr 1`\
`add y y 1`\
`branch 9`\
`done`

`sub c c 1`\
`printr 0`\
`branch 9`

This code is "Good code" because it respects the law of `branch`. The law states that a label must be declared and already
stored in a dict with its index--like the jump to point. This code always allows `label_1:` to be stored with its index
and when it is called, there is no error.

In the DNA data above, this "Good code" has passed runs tested on all Read Indexes. Read Index **4** or `@4` has the catch
and I show this later.

**Bad code**\
`set x a`\
`// AT counter`\
`set y 0`

`label_1:`

`if - A`\
`branch 23`\
`label_2:`\
`done`

`sub x x 1`\
`add c c 1`

`if c a`\
`stop`\
`done`

`if x 0`\
`stop`\
`done`\
`branch label_1`

`if c a`\
`stop`\
`done`

`printr 1`\
`add c c 1`

`if c a`\
`stop`\
`done`

`if - T`\
`printr 1`\
`add y y 1`\
`branch label_2`\
`done`

`sub c c 1`\
`printr 0`\
`branch label_2`

In the "Bad code" when Read Index **4** or `@4` is tested, since its data starts with `AT...` the code commands that when
`if - A` is true--which is true--`branch 23`. The catch is clear here that `label_2:` was not stored in available labels
which will cause an error when the program reaches `branch label_2` since `label_2` was not stored with its index.

This indicates that when using labels, user (you) must make a situation for this label to first be stored or declared like
the "Good code" implements it, then user (you) can call the label whenever user (you) wish.

**It works well with other Read Indexes**

![Screenshot 2026-08-13 at 10.58.49.png](addons/Screenshot%202026-08-13%20at%2010.58.49.png)

**But fails on pitfall(s)**

![Screenshot 2026-08-13 at 10.56.50.png](addons/Screenshot%202026-08-13%20at%2010.56.50.png)

**While on the other hand, the "Good code" nails both scenarios**

![Screenshot 2026-08-13 at 11.15.58.png](addons/Screenshot%202026-08-13%20at%2011.15.58.png)

![Screenshot 2026-08-13 at 11.11.47.png](addons/Screenshot%202026-08-13%20at%2011.11.47.png)


**"Functions"**

In Decode, user (you) can implement "Functions" using `branch`, labels, `if` statements, and setting variables.

`set m 0`\
`set n 0`

`label_1:`\
`if m 1`\
`printr 1`\
`branch n`\
`done`\
`set m 1`

`set n 14`\
`branch label_1`

`set z 0`\
`add z z 1`\
`sub m m 1`\
`if m -1`\
`branch 22`\
`done`\
`branch 15`

`set m 1`\
`add c c 1`

`set n 27`\
`branch label_1`\
`stop`

The program starts with variables `m` and `n` then creates a label called `label_1`.\
User (you) must put code in the label inside an `if` statement and deliberately set the condition to **not run** (False).
Then `set m 1` will make the condition **True** next time.\
Now `n` stores where the "function" will "return" to.
Call the "function" `label_1`.

Since the condition was made **True** by `set m 1`, the "function" will `printr 1` then "return".\
When the "function returns", it will return at `set z 0` and the code execution will continue.\
After `branch 22` jumps to `set m 1` the condition in the "function" `label_1` is made **True** and the program moves
ahead in data by 1 `add c c 1`; then sets the **return to point** to code index 27 and calls the "function" `label_1`\
After the "function" ends, it returns to code index 27 which has `stop`


## Example Usage For Decode Code That Shows Only "AT" Nucleotides In DNAGenre

`set x a`\
`// AT counter`\
`set y 0`

`if c a`\
`stop`\
`done`

`when x`

`if - A`\
`branch 23`\
`done`

`sub x x 1`\
`add c c 1`

`if c a`\
`stop`\
`done`

`end`

`if c a`\
`stop`\
`done`

`printr 1`\
`add c c 1`

`if c a`\
`stop`\
`done`

`if - T`\
`printr 1`\
`add y y 1`\
`branch 13`\
`done`

`sub c c 1`\
`printr 0`\
`branch 13`

**Notes**\
**I.** `y` counts how many times `AT` has been found in the sequence but never considers the last `A` because that last `A`
is NOT followed by a `T` (that last occurrence does not meet the task's demands).


**II.** This program focused on finding `AT` k-mer(s); other variations of this program that are tasked to find k-mers like
`AA`, `TT`, `GG`, `CC` in case of `AAA` this program will only identify the first two `A`s and not identifying the next two `A`s.
This is because as it is tasked to check for 2 nucleotides (`AA`) whenever this program finds an `A` it proceeds to one step forward to
see if there is another `A` and if it does not find another `A` to make `AA` as the task **demands**, it back tracks one step
and erases any highlights--regardless of what nucleotide was highlighted--which affects the last two `A`s in `AAA`.\
**III.** This program works well with `AAAA` because `AAAA` k-mer has two pairs of `AA` and if you (user) read **Note 2** that shows how this program works
this scenario is convenient for this program because this program finds an `A` and checks forward one step and finds another `A` which forms `AA`
and repeats this for the next two `A`s hence `AAAA` is highlighted.\
**IV.** One quick note is that this program works as expected with even-length k-mers
like `AA`, `AAAA`, `AAAAAA` but not `AAA`, `AAAAA`, `AAAAAAA` though it works well for one-length k-mer like `A`.


**V.** As I was doing these 39 lines of code, I realized after debugging that checking bounds is key, my language is verbose,
and spacing makes the language more readable. It was tough to write this one and I realize clearly that it is worse than Assembly but at least it got
a simple task done.


**VI.** DNAGenre saves user code in a file called `user_code.txt` for future use.

## Updated Version For Decode Code That Shows Only "AT" Nucleotides In DNAGenre

`set x a`\
`set y 0`\
`set m 0`\
`set n 0`

`label_1:`\
`if c a`\
`stop`\
`done`\
`if m 1`\
`branch n`\
`done`

`when x`

`if - A`\
`branch 28`\
`done`

`sub x x 1`\
`add c c 1`

`set n 27`\
`set m 1`\
`branch label_1`

`end`

`set n 32`\
`set m 1`\
`branch label_1`

`printr 1`\
`add c c 1`

`set n 38`\
`branch label_1`

`if - T`\
`printr 1`\
`add y y 1`\
`branch 18`\
`done`

`sub c c 1`\
`printr 0`\
`branch 18`


**No Data In Read Indexes**

The selected Read Index `11` in this scenario has no data at all. In Decode whenever user (you) tries to access the nucleotide in
data at index `c`, `c` must be within bounds of the length of that data. Since there is no data at all at Read Index `11`, accessing nucleotide at index `c`--even
though `c` has a value of `0` for now--causes an `out_of_bounds` error.

**Note: This also happens if Read Index has invalid data.**

![Screenshot 2026-08-12 at 13.14.37.png](addons/Screenshot%202026-08-12%20at%2013.14.37.png)

**13. Encryption And Decryption**

DNAGenre encrypts files when user closes program--it does not encrypt files when it is stopped by the operating system or in general is stopped
as a process somehow like shutting down.

**I. Below is how to close DNAGenre to encrypt files.**

![Screenshot 2026-08-01 at 09.41.21.png](addons/Screenshot%202026-08-01%20at%2009.41.21.png)

By pressing the close button (typically red), the program ends and branches into encryption of files. The `user_database.db`, `usage_database.db`, and `user_code.txt`
are the files encrypted. The keys are stored in files in a folder called **secure** even though there are better and safer ways to store the keys. I just
picked this one because it is simple to learn, implement, and contains some skills I knew in ARM Assembly.

**II. In case this happens, the best and recommended fix is to have the required files with keys exist then empty them (delete all text in the file).
Even though these files `user_database.db`, `usage_database.db`, and `user_code.txt` may have data or not, it is fine. As long as the required files
with the keys exist and are emptied.**

![Screenshot 2026-08-01 at 09.47.50.png](addons/Screenshot%202026-08-01%20at%2009.47.50.png)

**Warning Regarding Encryption And Decryption**

**I.** Whatever data is in these files `user_database.db`, `usage_database.db`, and `user_code.txt` when the files with the keys are recreated or created,
the data inside them (the files to be encrypted) is deemed as the data to be encrypted. If these files `user_database.db`, `usage_database.db`, and `user_code.txt` were encrypted and keys are lost,
that data in those files is encrypted again which proves that data is lost.

**II.** During a time when user (you) is using the program, the data in these files `user_database.db`, `usage_database.db`, and `user_code.txt` is unencrypted (literal plain text).
Decryption at the beginning then use literal plain text till user (you) ends the program as instructed finally the file's data can be encrypted.

**14. Compression**

In DNAGenre, I chose to use **2-bit compression** because it was simple to learn and fitted the project. 2-bit compression is when
a program uses 2-bits in a byte to store a full byte like in byte `00000000`; DNAGenre can store 4 bytes `A,T/U,G,C` into a single
byte because it can pack `A,T,G,C` into a single byte while in **DNA mode** or pack `A,U,G,C` into a single byte while in **RNA mode**.
This has given DNAGenre good compression of valid data.

**MeloPress** gets read index by read index and compresses that read index and writes the result to a file with a **file magic** and **file header**.
This makes it slow but results are very trustworthy.

DNAGenre's **MeloPress** can compress files with an improper length. All it does is that it compresses as usual but when writing that file of that
read index, it indicates systemically in the **file header** that this very file has an improper length.\
If user (you) tries to decompress a file in **compressed chunks folder** as standalone by using the `Decompress`
button, **MeloPress** will decompress only that file hence make sure to  `D Chunk` the first file in **compressed chunks folder** to
decompress the entire files in the **compressed chunks folder** into one file and `Decompress` any valid file for standalone decompression.

The `Compress` button allows user (you) to compress a file with some DNA/RNA data in it but when that data in decompressed, that
invalid data is lost and only the valid data--DNA/RNA--remains.

The `Decompress` button allows user (you) to decompress a file with compressed data.

The `Make DNAGenre` button allows user to take any file and make it adhere to DNAGenre format (Check Usage Under File Format).

The `D Chunk` button allows user to decompress files in **compressed chunk folder** into one file (Check Description About DNAGenre's MeloPress).

### Layout

![Screenshot 2026-08-22 at 09.56.56.png](addons/Screenshot%202026-08-22%20at%2009.56.56.png)

**I.** User (you) can open any file to start compress it.
![Screenshot 2026-08-08 at 12.46.47.png](addons/Screenshot%202026-08-08%20at%2012.46.47.png)

**II.** User (you) can view any compressed file to start to decompress it.
![Screenshot 2026-08-08 at 12.47.43.png](addons/Screenshot%202026-08-08%20at%2012.47.43.png)

**III.** User (you) can open a decompressed file and start to format it to DNAGenre format.
![Screenshot 2026-08-08 at 12.48.28.png](addons/Screenshot%202026-08-08%20at%2012.48.28.png)

**IV.** User (you) can view DNAGenre formatted file.
![Screenshot 2026-08-08 at 12.50.13.png](addons/Screenshot%202026-08-08%20at%2012.50.13.png)

### Warning

**1. Imagine User Wants To Work With An Incompatible File Like Below.**

![Screenshot 2026-08-12 at 16.28.51.png](addons/Screenshot%202026-08-12%20at%2016.28.51.png)

In my function that prepares DNA/RNA data from a selected file uses a dictionary. A Python Dictionary does not allow
duplicate keys but allows duplicate values. In such a file that seems to have `@` in each "Read Index", these "Read Indexes"
are duplicates of each other in a literal sense which makes the Python Dictionary to overwrite previous data for "Read Index"
`@`.

**This makes DNAGenre consider this as the valid data to work with.**

{'@': 'GAAGCTAGCTATTAGCTAGAGACCAGTAGCTCAGAGAGTAAATTGTAGCTAGCTAAGCGCCTTT'}

![Screenshot 2026-08-12 at 16.33.49.png](addons/Screenshot%202026-08-12%20at%2016.33.49.png)

If user decides to continue with this file in such a format, below is what happens.

![Screenshot 2026-08-12 at 16.34.10.png](addons/Screenshot%202026-08-12%20at%2016.34.10.png)

```
{
    "Seq(s) Length": 64,
    "Nucleotide Count": {
        "A": 20,
        "T": 16,
        "G": 16,
        "C": 12
    },
    "Mean Nuc Count": 16.0,
    "Median Nuc Count": 16.0,
    "Mode Nuc Count": 16,
    "Range Nuc Count": 8,
    "AC Percentage": 50.0,
    "AT Percentage": 56.25,
    "AU Percentage": 0.0,
    "AG Percentage": 56.25,
    "CT Percentage": 43.75,
    "CU Percentage": 0.0,
    "CG Percentage": 43.75,
    "TG Percentage": 50.0,
    "UG Percentage": 0.0,
    "GC Content Per Read Index": {
        "1": 43.75
    },
    "AT Content Per Read Index": {
        "1": 56.25
    },
    "AU Content Per Read Index": 0.0,
    "P(A)": 0.31,
    "P(T)": 0.25,
    "P(U)": 0.0,
    "P(G)": 0.25,
    "P(C)": 0.19,
    "P(Sequence Start is A)": 0.0,
    "P(Sequence Start is T)": 0.0,
    "P(Sequence Start is U)": 0.0,
    "P(Sequence Start is G)": 1.0,
    "P(Sequence Start is C)": 0.0,
    "P(Sequence End is A)": 0.0,
    "P(Sequence End is T)": 1.0,
    "P(Sequence End is U)": 0.0,
    "P(Sequence End is G)": 0.0,
    "P(Sequence End is C)": 0.0
}
```

**Note:**\
**I.** Only valid data is considered and in this case only this\
{'@': 'GAAGCTAGCTATTAGCTAGAGACCAGTAGCTCAGAGAGTAAATTGTAGCTAGCTAAGCGCCTTT'}\
**is what was and is considered.**

**II.** The only solution is to use `Make DNAGenre` button at this stage after decompression or even
to make the file have the compatible format.

Before `Make DNAGenre`
![Screenshot 2026-08-12 at 16.28.51.png](addons/Screenshot%202026-08-12%20at%2016.28.51.png)

After `Make DNAGenre`

![Screenshot 2026-08-12 at 17.00.16.png](addons/Screenshot%202026-08-12%20at%2017.00.16.png)

**2. Compressing A File With Improper File Length**

![Screenshot 2026-08-22 at 10.45.53.png](addons/Screenshot%202026-08-22%20at%2010.45.53.png)

After compression, **MeloPress** produces files that store chunks of the main uncompressed file--these 
chunks store compressed data of the main file though.

![Screenshot 2026-08-22 at 10.47.49.png](addons/Screenshot%202026-08-22%20at%2010.47.49.png)
![Screenshot 2026-08-22 at 10.48.09.png](addons/Screenshot%202026-08-22%20at%2010.48.09.png)

Pressing `D Chunks` decompresses the files in the respective **compressed chunks folder**. Always look for the first file
that is often labeled `1.fgh` and `D Chunk` that file.
![Screenshot 2026-08-22 at 10.48.45.png](addons/Screenshot%202026-08-22%20at%2010.48.45.png)

After `D Chunk` decompresses the files in **compressed chunks folder**, it produces one file that has the decompressed data.
![Screenshot 2026-08-22 at 10.51.51.png](addons/Screenshot%202026-08-22%20at%2010.51.51.png)


### Big Notes
**I.** When entering a Read Index to start hamming, k_mer search, or k_mer length, just enter a number (like `1` or `2`) this is
used as a reference that the user wants the sequence in read index number `1` or read index number `2`. Do not use `@1` or `@2` depending on what
read index you want, just use `1` or `2` or whatever read index you want but without other characters (in this case those
characters are `@` just type in a number). This is because I just realized that dictionaries do not allow duplicate keys
but allow duplicate values. Imagine user file has duplicate keys for read index hence wrong data generated. I have decided
to use numbers because numbers never repeat as a **counter** counts on.


**II.** User can export--in a window with the export button--data generated by DNAGenre into a JSON formated file for standard usage in other programs.
1. **Look for a button that says `Export`.**

2. **Press it to update a file called `current_export.json` created by the DNAGenre.**
\
![Screenshot 2026-07-27 at 21.24.12.png](addons/Screenshot%202026-07-27%20at%2021.24.12.png)

3. **Below is an example of an export.**
\
\
![Screenshot 2026-07-27 at 21.24.51.png](addons/Screenshot%202026-07-27%20at%2021.24.51.png)


**III.** The reason there is no button that takes user (you) back to sign in window is because **DNAGenre** treats every account on disk as a virtual machine.
Every user starts fresh and uses their state. If that user (you) wants to switch users or sign in another user, they must close the app (state) and
begin a new state. This guarantees that variables, state, and sensitive data are not accidentally leaked to another signed-in user.

**IV.** When compression and decompression execute, "unnecessary data" is lost like read index descriptions etc. While important data like the DNA/RNA nucleotides
(data) is preserved. **MeloPress** can only compress **A,T/U,G,C** characters **not including the special characters**: **newline** and `@`--because they are added later
as designs for readability. This makes the program discard invalid characters and preserve valid characters.

**V.** **MeloPress** is very slow at compressing but very fast at decompressing. There was a method of using **markers** (Check previous
GitHub Versions) that allowed **MeloPress** to compress data faster but produced inaccurate results in some scenarios. This current approach is slow but produces
very trustworthy results.

**VI.** Since there are different combinations for a byte, a user (you) can just make a `.fgh` file. Following this then adds the file magic `#H9`. After that,
these bytes could bypass security: (`F`-symbol, `01000110`-bin, `46`-hex, `106`-oct, `70`-dec, `Uppercase F`-description); (`ACK`-symbol, `00000110`-bin, `06`-hex,
`006`-oct, `6`-dec, `Acknowledge`-description) etc. With this well crafted, user (you) can bypass security and achieve results like DNAGenre saying that this file
is compressed and yet it is not. I use file headers which are not perfect in my scenario but if anyone has a better way, please reach out through the contacts in the contact section.



## Tech Stack ##
```
Pycharm - Code Editor
ChatGPT - AI Assistant
Google's AI Mode - AI Assistant
```

I am very fluent with prompting most Large Language Models(LLMs) because I use patterns in my prompts, simple prompts and
most notably use words that cause attention hence push AI to reason.

For example;
I want ChatGPT to give me an essay for a college application

I would say

    Hey, What's up, I would love a well-polished college essay like those college essays in
    the early 2000s.

    Instructions
    1. Use simple English
    2. Use less words
    3. Use 2025 college essay structure

Explanation;
When I say `Hey, What's up` the model tunes its attention to a 'sweet mode' and will reason nicely and happily (due to
inbuilt ethical restrictions you may see that when it is nice but not when it is angry)

When I add `I would love a well-polished college essay` the word `I would love` sharpens it niceness and the word
`a well-polished essay` makes it pick a good essay out of those in its brain.

When I add `like those college essays in the early 2000s` it takes the models attention to college essays written in
the early 2000s (I do this because college essays by then have changed over time and this makes humans not even close
to thinking it was AI). It will use the slang and language by then hence I can edit the output essay to an appropriate level.

`Use simple English` this amplifies the 2000 timeline produced college essay
`Use less words` this makes the model use less word but if I said `Use 200-500 words`, I am using the data of today mostly
which will bring it back to 2025, yet I want something way back like 2000s.
`Use 2025 college essay structure` this will bring it back to 2025 after carrying everything from 2000s (our college essay)
and just make it look like 2025.

Here is what ChatGPT gave me, no reasoning just ChatGPT (great for everyday tasks)

```
When I was twelve, I broke apart my family’s old computer. Everyone thought I had ruined it,
but I wasn’t trying to destroy anything. I wanted to know how it worked. The wires, the
circuits, the dust inside—it all looked like a puzzle waiting to be solved. I didn’t fix
the computer that day, but I fixed something in myself: my fear of breaking things.

Since then, I’ve treated learning as a kind of tinkering. When I study math, I pull apart formulas
to see how each step fits. When I write code, I test lines until they fail, then rebuild.
Even in conversations, I ask questions that make people pause, as if I’ve unscrewed a piece
of their thought. For me, mistakes are not dead ends—they are the screws on the floor,
proof that I’m working toward understanding. 

Still, curiosity can be lonely. Friends sometimes tease me for “thinking too much.”
But I’ve learned to see this as a strength. It’s what helps me stay with a hard problem until it finally clicks.
It’s also what makes me want to study computer science in college: a field where asking “what if” is not only allowed,
but required. 

I want to be the kind of person who doesn’t just use technology but shapes
it—who builds tools that make life simpler, smarter, or fairer. I know I’ll keep breaking
things apart, whether it’s code, ideas, or assumptions. But now, I break them with
purpose: to build something better.
```


## Contributing ##
```
If you are interested in improving or upgrading this project even though you are a beginner or expert,
please feel free to contact me through my contacts in the contacts section.
```


## Copyright ##
```
If anyone wants to use this project for their project(s), education or work, please do freely.
Please feel at ease to either star the project or fork it just to show an appreciation
(It is optional to star or fork).
```


## Contact ##
```
It is very convenient to reach out to me through these contacts below because I can answer
within minutes.
```
LinkedIn - [My LinkedIn](https://www.linkedin.com/in/imboowa/)