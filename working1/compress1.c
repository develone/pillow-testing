#include <stdio.h>
#include <stdlib.h>

const char * outputfiles[] = {
"IMG_0097.j2k","IMG_0101.j2k","IMG_0110.j2k","IMG_0113.j2k","IMG_0115.j2k","IMG_0116.j2k","IMG_0146.j2k","IMG_0161.j2k","IMG_0337.j2k","IMG_0396.j2k","IMG_0478.j2k","IMG_0504.j2k","IMG_0505.j2k","IMG_0524.j2k","IMG_0529.j2k","IMG_0585.j2k","IMG_1021.j2k","IMG_1022.j2k","IMG_1044.j2k","IMG_1047.j2k","IMG_1062.j2k","IMG_1064.j2k","IMG_1164.j2k","IMG_1181.j2k","IMG_1183.j2k","IMG_1189.j2k","IMG_1191.j2k","IMG_1201.j2k","IMG_1203.j2k","IMG_1208.j2k","IMG_1223.j2k","IMG_1235.j2k","IMG_1237.j2k","IMG_1243.j2k","IMG_1245.j2k","IMG_1298.j2k","IMG_1321.j2k","IMG_1323.j2k","IMG_1324.j2k","IMG_1325.j2k","IMG_1387.j2k","IMG_1394.j2k","IMG_1396.j2k","IMG_1399.j2k","IMG_1401.j2k","IMG_1417.j2k","IMG_1421.j2k","IMG_1422.j2k","IMG_1642.j2k","IMG_1649.j2k","IMG_1656.j2k","IMG_1657.j2k","IMG_1673.j2k","IMG_1759.j2k","IMG_1827.j2k","IMG_1901.j2k","IMG_1925.j2k","IMG_1926.j2k","IMG_1927.j2k","IMG_1978.j2k","IMG_2009.j2k","IMG_2069.j2k","IMG_2071.j2k","IMG_2115.j2k","IMG_2117.j2k","IMG_2126.j2k","IMG_2212.j2k","IMG_2290.j2k","IMG_2305.j2k","IMG_2319.j2k","IMG_2324.j2k","IMG_2385.j2k","IMG_2480.j2k","IMG_2506.j2k","IMG_2535.j2k","IMG_2536.j2k","IMG_2538.j2k","IMG_2539.j2k","IMG_2540.j2k","IMG_2541.j2k","IMG_2542.j2k","IMG_2637.j2k","IMG_3295.j2k","IMG_3296.j2k","IMG_3791.j2k","IMG_4331.j2k"
};
const char * inputfiles[] = {
"IMG_0097.png","IMG_0101.png","IMG_0110.png","IMG_0113.png","IMG_0115.png","IMG_0116.png","IMG_0146.png","IMG_0161.png","IMG_0337.png","IMG_0396.png","IMG_0478.png","IMG_0504.png","IMG_0505.png","IMG_0524.png","IMG_0529.png","IMG_0585.png","IMG_1021.png","IMG_1022.png","IMG_1044.png","IMG_1047.png","IMG_1062.png","IMG_1064.png","IMG_1164.png","IMG_1181.png","IMG_1183.png","IMG_1189.png","IMG_1191.png","IMG_1201.png","IMG_1203.png","IMG_1208.png","IMG_1223.png","IMG_1235.png","IMG_1237.png","IMG_1243.png","IMG_1245.png","IMG_1298.png","IMG_1321.png","IMG_1323.png","IMG_1324.png","IMG_1325.png","IMG_1387.png","IMG_1394.png","IMG_1396.png","IMG_1399.png","IMG_1401.png","IMG_1417.png","IMG_1421.png","IMG_1422.png","IMG_1642.png","IMG_1649.png","IMG_1656.png","IMG_1657.png","IMG_1673.png","IMG_1759.png","IMG_1827.png","IMG_1901.png","IMG_1925.png","IMG_1926.png","IMG_1927.png","IMG_1978.png","IMG_2009.png","IMG_2069.png","IMG_2071.png","IMG_2115.png","IMG_2117.png","IMG_2126.png","IMG_2212.png","IMG_2290.png","IMG_2305.png","IMG_2319.png","IMG_2324.png","IMG_2385.png","IMG_2480.png","IMG_2506.png","IMG_2535.png","IMG_2536.png","IMG_2538.png","IMG_2539.png","IMG_2540.png","IMG_2541.png","IMG_2542.png","IMG_2637.png","IMG_3295.png","IMG_3296.png","IMG_3791.png","IMG_4331.png"
};

int main() {
	int i;
	int x = sizeof(inputfiles);
	//printf("%d\n",x); 
	printf("#!/bin/bash\n");
	for (i=0;i<x;i++) {
		//system("mycmd");
		printf("./opj_compress -i %s -r 150  -o %s\n",inputfiles[i],outputfiles[i]);
                //system("./obj_compress -i inputfiles[i] -r 150 -o outputfiles[i]");
	}
}

