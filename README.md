# acms80870_project_palathinkal

This repo is to study the path loss (PL) modelling for radio systems working in the CBRS band (3550-3700 MHz).

For this, measurements were collected using smartphones (also called user-equipments (UEs)), and these measurements are analyzed to extract received signal strenght measurements.

As expected, the measurements are not perfect, and cleaning process needs to be performed before using it to statistical model path loss.

For context, in 2015, the FCC established CBRS 1.0 for sharing the 3.5 GHz Band (3550-3700 MHz) among federal and non-federal users in the United States. This rulemaking was implemented in a novel three-tier rights structure (as shown in Fig.):
1. strong protections for incumbents, including government radar systems;
2. PALs granting exclusive rights to high bidders in an FCC auction, subject to avoiding interference with incumbents; and
3. GAA for unlicensed users, subject to avoiding interference with both PALs and incumbents.

![cbrs_license](/documentation/cbrs_license.png)
Three-tier hierarchical architecture of CBRS band.

<figure>
    <img src="/documentation/cbrs_license.png"
         alt="cbrs_license">
    <figcaption>Three-tier hierarchical architecture of CBRS band.</figcaption>
</figure>