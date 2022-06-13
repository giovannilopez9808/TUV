# TUV

## Input file format

The file `data.txt` must be outside of `src` folder with this format

|      Input file       |         Date          | tauaer | Ozone |  Year   |  Month  | Day     | Initial hour | Final hour |
| :-------------------: | :-------------------: | :----: | :---: | :-----: | :-----: | ------- | ------------ | ---------- |
| String (3 characters) | String (6 characters) | float  | float | Integer | Integer | Integer | Integer      | Integer    |

## Compilation results

`bash
gfortran -O -c numer.f
gfortran -O -c functs.f
gfortran -O -c orbit.f
gfortran -O -c terint.f
gfortran -O -c TUV.f
gfortran -O -c grids.f
gfortran -O -c rdinp.f
rdinp.f:282:0:

282 | finame = tmpfil(1:nlen)
|
Warning: ‘\_\_builtin_memcpy’ reading 20 bytes from a region of size 6 [-Wstringop-overflow=]
gfortran -O -c rdetfl.f
gfortran -O -c rdxs.f
gfortran -O -c swphys.f
gfortran -O -c swbiol.f
gfortran -O -c swchem.f
gfortran -O -c rxn.f
gfortran -O -c qys.f
gfortran -O -c wshift.f
gfortran -O -c vpair.f
gfortran -O -c vptmp.f
gfortran -O -c vpo3.f
gfortran -O -c odrl.f
gfortran -O -c odo3.f
gfortran -O -c setalb.f
gfortran -O -c setcld.f
gfortran -O -c setsnw.f
gfortran -O -c setno2.f
gfortran -O -c seto2.f
gfortran -O -c setso2.f
gfortran -O -c sphers.f
gfortran -O -c la_srb.f
gfortran -O -c rtrans.f
rtrans.f:1352:55:

1352 | CALL LEPOLY( NCOS, MAZIM, MXCMU, NSTR - 1, ANGCOS, YLM0 )
| 1
Warning: Rank mismatch in argument ‘mu’ at (1) (rank-1 and scalar) [-Wargument-mismatch]
gfortran -O -c savout.f
gfortran -O -c newlst.f
gfortran -O -c wrflut.f
gfortran -O -c waters.f
gfortran -O -c swdom.f
gfortran -O -c setaer.f
gfortran -O numer.o functs.o orbit.o terint.o TUV.o grids.o rdinp.o rdetfl.o rdxs.o swphys.o swbiol.o swchem.o rxn.o qys.o wshift.o vpair.o vptmp.o vpo3.o odrl.o odo3.o setalb.o setcld.o setsnw.o setno2.o seto2.o setso2.o sphers.o la_srb.o rtrans.o savout.o newlst.o wrflut.o waters.o swdom.o setaer.o -o tuv.out
`
