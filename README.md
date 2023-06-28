# DockerRNA
DockerRNA is a project to create docker images for tools related to the analysis of RNA structure. The goal is to make it easier to use these tools by removing the need to install them and their dependencies. Along with the new docker images, the project also includes links to already existing docker images that are useful for RNA structure analysis. By having all of these images in one place, it will be easier to find the right tool for the job and incorporate them into future workflows. 

---

## Docker Images
<details><summary><a>RNABOB</a></summary>

## RNAbob

### Link to image:
```
kjkirven/rnabob:latest
```

### Usage
```
rnabob -h
```

### Citation 
```
Rampášek, L., Jimenez, R.M., Lupták, A. et al. RNA motif search with data-driven element ordering. BMC Bioinformatics 17, 216 (2016). https://doi.org/10.1186/s12859-016-1074-x
```
</details>


<details><summary><a>RNArobo</a></summary>

## RNArobo

### Link to image:
```
kjkirven/rnarobo:latest
```

### Usage
```
rnarobo -h
```

### Citation 
```
Rampášek, L., Jimenez, R.M., Lupták, A. et al. RNA motif search with data-driven element ordering. BMC Bioinformatics 17, 216 (2016). https://doi.org/10.1186/s12859-016-1074-x
```
</details>


<details><summary><a>ScanFold</a></summary>

## ScanFold

### Link to image:
```
kjkirven/scanfold:latest
```

### Usage
```
python3 /data2/ScanFold/ScanFold.py
```

### Citation 
```
Andrews RJ, Roche J, Moss WN. ScanFold: an approach for genome-wide discovery of local RNA structural elements-applications to Zika virus and HIV. PeerJ. 2018 Dec 18;6:e6136. doi: 10.7717/peerj.6136. PMID: 30627482; PMCID: PMC6317755.
```
</details>

## Contributing
If you have a tool that you would like to see added to this project, please open an issue or submit a pull request (see CONTRIBUTING.md).