# TUV

## Input file format

The file name must be outside of `src` folder with this format

|      Input file       |         Date          | tauaer | Ozone |  Year   |  Month  | Day     | Initial hour | Final hour |
| :-------------------: | :-------------------: | :----: | :---: | :-----: | :-----: | ------- | ------------ | ---------- |
| String (3 characters) | String (6 characters) | float  | float | Integer | Integer | Integer | Integer      | Integer    |

## Compilation results

```bash
gfortran -O3 -c functs.f
gfortran -O3 -c orbit.f
gfortran -O3 -c terint.f
gfortran -O3 -c TUV.f
gfortran -O3 -c grids.f
gfortran -O3 -c rdinp.f
gfortran -O3 -c rdetfl.f
gfortran -O3 -c rdxs.f
gfortran -O3 -c swphys.f
gfortran -O3 -c swbiol.f
gfortran -O3 -c swchem.f
gfortran -O3 -c rxn.f
gfortran -O3 -c qys.f
gfortran -O3 -c wshift.f
gfortran -O3 -c vpair.f
gfortran -O3 -c vptmp.f
gfortran -O3 -c vpo3.f
gfortran -O3 -c odrl.f
gfortran -O3 -c odo3.f
gfortran -O3 -c setaer.f
gfortran -O3 -c setalb.f
gfortran -O3 -c setcld.f
gfortran -O3 -c setsnw.f
gfortran -O3 -c setno2.f
gfortran -O3 -c seto2.f
gfortran -O3 -c setso2.f
gfortran -O3 -c sphers.f
gfortran -O3 -c la_srb.f
gfortran -O3 -c rtrans.f
rtrans.f:1352:55:

 1352 |             CALL LEPOLY( NCOS, MAZIM, MXCMU, NSTR - 1, ANGCOS, YLM0 )
      |                                                       1
Warning: Rank mismatch in argument ‘mu’ at (1) (rank-1 and scalar) [-Wargument-mismatch]
gfortran -O3 -c savout.f
gfortran -O3 -c newlst.f
gfortran -O3 -c wrflut.f
gfortran -O3 -c waters.f
gfortran -O3 -c swdom.f
gfortran -O3 numer.o functs.o orbit.o terint.o TUV.o grids.o rdinp.o rdetfl.o rdxs.o swphys.o swbiol.o swchem.o rxn.o qys.o wshift.o vpair.o vptmp.o vpo3.o odrl.o odo3.o setaer.o setalb.o setcld.o setsnw.o setno2.o seto2.o setso2.o sphers.o la_srb.o rtrans.o savout.o newlst.o wrflut.o waters.o swdom.o   -o tuv.out
```
