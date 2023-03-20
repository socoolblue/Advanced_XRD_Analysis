import numpy as np
import os
import subprocess
import shutil
import time
import matplotlib.pyplot as plt

# Space Group of All

sg_std = np.empty((231, 29), dtype=object)

#Triclnic
sg_std[1,0:6] = ["P 1","A 1", "B 1","C 1","F 1","I 1"]
sg_std[2,0:6] = ["P -1","A -1", "B -1","C -1","F -1","I -1"]

#Monoclinic
sg_std[3,0:6] = ["P 1 2 1","P 1 1 2","P 2 1 1","C 1 1 2","P 2 1 1","A 2 1 1"]
sg_std[4,0:6] = ["P 1 21 1","B 1 21 1","P 1 1 21","C 1 1 21","P 21 1 1","A 21 1 1"]
sg_std[5,0:12] = ["C 1 2 1","A 1 2 1","I 1 2 1","F 1 2 1","A 1 1 2","B 1 1 2",
                  "I 1 1 2","F 1 1 2","B 2 1 1","C 2 1 1","I 2 1 1","F 2 1 1"]
sg_std[6,0:6] = ["P 1 m 1","B 1 m 1","P 1 1 m","C 1 1 m","P m 1 1","A m 1 1"]
sg_std[7,0:15] = ["P 1 c 1","P 1 a 1","P 1 n 1","B 1 a 1","B 1 d 1","P 1 1 a",
                  "P 1 1 b","P 1 1 n","C 1 1 a","C 1 1 d","P b 1 1","P c 1 1",
                  "P n 1 1","A b 1 1","A d 1 1"]
sg_std[8,0:12] = ["C 1 m 1","A 1 m 1","I 1 m 1","F 1 m 1","A 1 1 m","B 1 1 m",
                  "I 1 1 m","F 1 1 m","B m 1 1","C m 1 1","I m 1 1","F m 1 1"]
sg_std[9,0:21] = ["C 1 c 1","A 1 n 1","I 1 a 1","A 1 a 1","C 1 n 1","I 1 c 1",
                  "A 1 1 a","B 1 1 n","I 1 1 b","B 1 1 b","A 1 1 n","I 1 1 a",
                  "B b 1 1","C n 1 1","I c 1 1","C c 1 1","B n 1 1","I b 1 1",
                  "F d 1 1","F 1 d 1","F 1 1 d"]
sg_std[10,0:6] = ["P 1 2/m 1","B 1 2/m 1","P 1 1 2/m","C 1 1 2/m","P 2/m 1 1","A 2/m 1 1"]
sg_std[11,0:6] = ["P 1 21/m 1","B 1 21/m 1","P 1 1 21/m","C 1 1 21/m","P 21/m 1 1","A 21/m 1 1"]
sg_std[12,0:12] = ["C 1 2/m 1","A 1 2/m 1","I 1 2/m 1","F 1 2/m 1","A 1 1 2/m","B 1 1 2/m",
                   "I 1 1 2/m","F 1 1 2/m","B 2/m 1 1","C 2/m 1 1","I 2/m 1 1","F 2/m 1 1"]
sg_std[13,0:16] = ["P 1 2/c 1","P 1 2/a 1","P 1 2/n 1","B 1 2/a 1","B 1 2/d 1","P 1 1 2/a",
                   "P 1 1 2/b","P 1 1 2/n","C 1 1 2/a","C 1 1 2/d","P 2/b 1 1","P 2/c 1 1",
                   "P 2/n 1 1","A 2/b 1 1","A 2/d 1 1","B 1 2/c 1"]
sg_std[14,0:16] = ["P 1 21/c 1","P 1 21/n 1","P 1 21/a 1","P 1 1 21/a","P 1 1 21/n","P 1 1 21/b",
                   "P 21/b 1 1","P 21/n 1 1","P 21/c 1 1","B 1 21/a 1","B 1 21/d 1","C 1 1 21/a",
                   "C 1 1 21/d","A 21/b 1 1","A 21/d 1 1","B 1 21/c 1"]
sg_std[15,0:23] = ["C 1 2/c 1","A 1 2/n 1","I 1 2/a 1","A 1 2/a 1","C 1 2/n 1","I 1 2/c 1",
                   "A 1 1 2/a","B 1 1 2/n","I 1 1 2/b","B 1 1 2/b","A 1 1 2/n","I 1 1 2/a",
                   "B 2/b 1 1","C 2/n 1 1","I 2/c 1 1","C 2/c 1 1","B 2/n 1 1","I 2/b 1 1",
                   "F 1 2/d 1","F 2/d 1 1","F 1 1 2/d","A 1 2/a 1 S","I 1 1 2/a S"]

#Orthorhombic
sg_std[16,0:1] = ["P 2 2 2"] 
sg_std[17,0:3] = ["P 2 2 21","P 2 21 2","P 21 2 2"] 
sg_std[18,0:3] = ["P 21 21 2","P 21 2 21","P 2 21 21"] 
sg_std[19,0:1] = ["P 21 21 21"] 
sg_std[20,0:7] = ["C 2 2 21","C 2 2 21","B 2 21 2","B 2 21 2","A 21 2 2","A 21 2 2","C 2 2 21 S"]
sg_std[21,0:3] = ["C 2 2 2","B 2 2 2","A 2 2 2"] 
sg_std[22,0:1] = ["F 2 2 2"] 
sg_std[23,0:1] = ["I 2 2 2"] 
sg_std[24,0:1] = ["I 21 21 21"] 
sg_std[25,0:3] = ["P m m 2","P m 2 m","P 2 m m"] 
sg_std[26,0:6] = ["P m c 21","P c m 21","P b 21 m","P m 21 b","P 21 m a","P 21 a m"]
sg_std[27,0:3] = ["P c c 2","P b 2 b","P 2 a a"] 
sg_std[28,0:6] = ["P m a 2","P b m 2","P c 2 m","P m 2 a","P 2 m b","P 2 c m"]
sg_std[29,0:6] = ["P c a 21","P b c 21","P c 21 b","P b 21 a","P 21 a b","P 21 c a"]
sg_std[30,0:6] = ["P n c 2","P c n 2","P b 2 n","P n 2 b","P 2 n a","P 2 a n"]
sg_std[31,0:6] = ["P m n 21","P n m 21","P n 21 m","P m 21 n","P 21 m n","P 21 n m"]
sg_std[32,0:3] = ["P b a 2","P c 2 a","P 2 c b"] 
sg_std[33,0:6] = ["P n a 21","P b n 21","P c 21 n","P n 21 a","P 21 n b","P 21 c n"]
sg_std[34,0:3] = ["P n n 2","P n 2 n","P 2 n n"] 
sg_std[35,0:3] = ["C m m 2","B m 2 m","A 2 m m"] 
sg_std[36,0:6] = ["C m c 21","C c m 21","B b 21 m","B m 21 b","A 21 m a","A 21 a m"]
sg_std[37,0:3] = ["C c c 2","B b 2 b","A 2 a a"] 
sg_std[38,0:6] = ["A m m 2","B m m 2","C m 2 m","A m 2 m","B 2 m m","C 2 m m"]
sg_std[39,0:18] = ["A b m 2","B m a 2","C m 2 a","A b 2 m","B 2 a m","C 2 m a",
                  "A e m 2","B m e 2","C m 2 e","A e 2 m","B 2 e m","C 2 m e",
                  "A c m 2","B m c 2","C m 2 b","A c 2 m","B 2 c m","C 2 m b"]
sg_std[40,0:6] = ["A m a 2","B b m 2","C c 2 m","A m 2 a","B 2 m b","C 2 c m"]
sg_std[41,0:18] = ["A b a 2","B b a 2","C c 2 a","A b 2 a","B 2 a b","C 2 c a",
                  "A e a 2","B b e 2","C c 2 e","A e 2 a","B 2 e b","C 2 c e",
                  "A c a 2","B b c 2","C c 2 b","A c 2 a","B 2 c b","C 2 c b"]
sg_std[42,0:3] = ["F m m 2","F 2 m m","F m 2 m"] 
sg_std[43,0:3] = ["F d d 2","F d 2 d","F 2 d d"] 
sg_std[44,0:3] = ["I m m 2","I m 2 m","I 2 m m"] 
sg_std[45,0:3] = ["I b a 2","I b 2 a","I 2 a a"] 
sg_std[46,0:9] = ["I m a 2","I b m 2","I b 2 m","I m 2 a","I 2 m a","I 2 a m",
                  "I 2 m b","I 2 c m","I c 2 m"]
sg_std[47,0:1] = ["P m m m"] 
sg_std[48,0:3] = ["P n n n","P n n n Z","P n n n S"] 
sg_std[49,0:3] = ["P c c m","P b m b","P m a a"] 
sg_std[50,0:9] = ["P b a n","P n c b","P c n a","P b a n Z","P n c b Z","P c n a Z",
                  "P b a n S","P n c b S","P c n a S"]
sg_std[51,0:6] = ["P m m a","P m m b","P m c m","P m a m","P b m m","P c m m"]
sg_std[52,0:7] = ["P n n a","P n n b","P n c n","P n a n","P b n n","P c n n","P n a n S"]
sg_std[53,0:6] = ["P m n a","P n m b","P n c m","P m a n","P b m n","P c n m"]
sg_std[54,0:6] = ["P c c a","P c c b","P b c b","P b a b","P b a a","P c a a"]
sg_std[55,0:3] = ["P b a m","P c m a","P m c b"] 
sg_std[56,0:3] = ["P c c n","P b n b","P n a a"] 
sg_std[57,0:6] = ["P b c m","P c a m","P b m a","P c m b","P m c a","P m a b"]
sg_std[58,0:3] = ["P n n m","P n m n","P m n n"] 
sg_std[59,0:9] = ["P m m n","P m n m","P n m m","P m m n Z","P m n m Z","P n m m Z",
                  "P m m n S","P m n m S","P n m m S"] 
sg_std[60,0:6] = ["P b c n","P c a n","P b n a","P c n b","P n c a","P n a b"]
sg_std[61,0:2] = ["P b c a","P c a b"] 
sg_std[62,0:6] = ["P n m a","P n a m","P m c n","P c m n","P b n m","P m n b"]
sg_std[63,0:6] = ["C m c m","C c m m","B b m m","B m m b","A m m a","A m a m"]
sg_std[64,0:18] = ["C m c a","C c m a","A b m a","A b a m","B b a m","B m a b",
                   "C m c e","C c m e","A e m a","A e a m","B b e m","B m e b",
                   "C m c b","C c m b","A c m a","A c a m","B b c m","B m c b"]
sg_std[65,0:3] = ["C m m m","A m m m","B m m m"] 
sg_std[66,0:3] = ["C c c m","B b m b","A m a a"] 
sg_std[67,0:9] = ["C m m a","B m a m","A b m m","C m m e","A e m m","B m e m",
                  "C m m b","A c m m","B m c m"] 
sg_std[68,0:29] = ["C c c a","B b a b","A b a a","C c c e","A e a a","B b e b",
                  "C c c e","A e a a","B b e b","C c c a Z","B b a b Z","A b a a Z",
                  "C c c a S","B b a b S","A b a a S","C c c e Z","A e a a Z","B b e b Z",
                  "C c c e S","A e a a S","B b e b S","C c c b Z","A c a a Z","B b c b Z",
                  "C c c b S","A c a a S","B b c b S", "A c a a","B b c b"] 
sg_std[69,0:1] = ["F m m m"] 
sg_std[70,0:3] = ["F d d d","F d d d Z","F d d d S"] 
sg_std[71,0:1] = ["I m m m"] 
sg_std[72,0:5] = ["I b a m","I b m a","I m a a","I m c b","I c m a"] 
sg_std[73,0:1] = ["I b c a"] 
sg_std[74,0:6] = ["I m m a","I m m b","I b m m","I c m m","I m c m","I m a m"] 

#Tetragonal
sg_std[75,0:2] = ["P 4","C 4"]
sg_std[76,0:2] = ["P 41","C 41"]
sg_std[77,0:2] = ["P 42","C 42"]
sg_std[78,0:2] = ["P 43","C 43"]
sg_std[79,0:2] = ["I 4","F 4"]
sg_std[80,0:2] = ["I 41","F 41"]
sg_std[81,0:6] = ["P -4","C -4","P -4 Z","C -4 Z","P -4 S","C -4 S"]
sg_std[82,0:2] = ["I -4","F -4"]
sg_std[83,0:2] = ["P 4/m","C 4/m"]
sg_std[84,0:2] = ["P 42/m","C 42/m"]
sg_std[85,0:6] = ["P 4/n","C 4/a","P 4/n Z","C 4/a Z","P 4/n S","C 4/a S"]
sg_std[86,0:6] = ["P 42/n","C 42/a","P 42/n Z","C 42/a Z","P 42/n S","C 42/a S"]
sg_std[87,0:2] = ["I 4/m","F 4/m"]
sg_std[88,0:8] = ["I 41/a","F 41/d","I 41/a Z","F 41/d Z","I 41/a Z1","F 41/d Z1",
                  "I 41/a S","F 41/d S"]
sg_std[89,0:2] = ["P 4 2 2","C 4 2 2"]
sg_std[90,0:2] = ["P 4 21 2","C 4 2 21"]
sg_std[91,0:2] = ["P 41 2 2","C 41 2 2"]
sg_std[92,0:2] = ["P 41 21 2","C 41 2 21"]
sg_std[93,0:2] = ["P 42 2 2","C 42 2 2"]
sg_std[94,0:2] = ["P 42 21 2","C 42 2 21"]
sg_std[95,0:2] = ["P 43 2 2","C 43 2 2"]
sg_std[96,0:2] = ["P 43 21 2","C 43 2 21"]
sg_std[97,0:2] = ["I 4 2 2","F 4 2 2"]
sg_std[98,0:2] = ["I 41 2 2","F 41 2 2"]
sg_std[99,0:2] = ["P 4 m m","C 4 m m"]
sg_std[100,0:2] = ["P 4 b m","C 4 m b"]
sg_std[101,0:2] = ["P 42 c m","C 42 m c"]
sg_std[102,0:2] = ["P 42 n m","C 42 m n"]
sg_std[103,0:2] = ["P 4 c c","C 4 c c"]
sg_std[104,0:2] = ["P 4 n c","C 4 c n"]
sg_std[105,0:2] = ["P 42 m c","C 42 c m"]
sg_std[106,0:2] = ["P 42 b c","C 42 c b"]
sg_std[107,0:2] = ["I 4 m m","F 4 m m"]
sg_std[108,0:2] = ["I 4 c m","F 4 m c"]
sg_std[109,0:2] = ["I 41 m d","F 41 d m"]
sg_std[110,0:2] = ["I 41 c d","F 41 d c"]
sg_std[111,0:2] = ["P -4 2 m","C -4 m 2"]
sg_std[112,0:2] = ["P -4 2 c","C -4 c 2"]
sg_std[113,0:2] = ["P -4 21 m","C -4 m 21"]
sg_std[114,0:2] = ["P -4 21 c","C -4 c 21"]
sg_std[115,0:2] = ["P -4 m 2","C -4 2 m"]
sg_std[116,0:2] = ["P -4 c 2","C -4 2 c"]
sg_std[117,0:2] = ["P -4 b 2","C -4 2 b"]
sg_std[118,0:2] = ["P -4 n 2","C -4 2 n"]
sg_std[119,0:2] = ["I -4 m 2","F -4 2 m"]
sg_std[120,0:2] = ["I -4 c 2","F -4 2 c"]
sg_std[121,0:2] = ["I -4 2 m","F -4 m 2"]
sg_std[122,0:2] = ["I -4 2 d","F -4 d 2"]
sg_std[123,0:2] = ["P 4/m m m","C 4/m m m"]
sg_std[124,0:2] = ["P 4/m c c","C 4/m c c"]
sg_std[125,0:6] = ["P 4/n b m","C 4/a m b","P 4/n b m Z","C 4/a m b Z","P 4/n b m S","C 4/a m b S"]
sg_std[126,0:6] = ["P 4/n n c","C 4/a c n","P 4/n n c Z","C 4/a c n Z","P 4/n n c S","C 4/a c n S"]
sg_std[127,0:2] = ["P 4/m b m","C 4/m m b"]
sg_std[128,0:2] = ["P 4/m n c","C 4/m c n"]
sg_std[129,0:6] = ["P 4/n m m","C 4/a m m","P 4/n m m Z","C 4/a m m Z","P 4/n m m S","C 4/a m m S"]
sg_std[130,0:6] = ["P 4/n c c","C 4/a c c","P 4/n c c Z","C 4/a c c Z","P 4/n c c S","C 4/a c c S"]
sg_std[131,0:2] = ["P 42/m m c","C 42/m c m"]
sg_std[132,0:2] = ["P 42/m c m","C 42/m m c"]
sg_std[133,0:6] = ["P 42/n b c","C 42/a c b","P 42/n b c Z","C 42/a c b Z","P 42/n b c S","C 42/a c b S"]
sg_std[134,0:6] = ["P 42/n n m","C 42/a n m","P 42/n n m Z","C 42/a n m Z","P 42/n n m S","C 42/a n m S"]
sg_std[135,0:2] = ["P 42/m b c","C 42/m c b"]
sg_std[136,0:2] = ["P 42/m n m","C 42/m m n"]
sg_std[137,0:6] = ["P 42/n m c","C 42/a c m","P 42/n m c Z","C 42/a c m Z","P 42/n m c S","C 42/a c m S"]
sg_std[138,0:6] = ["P 42/n c m","C 42/a m c","P 42/n c m Z","C 42/a m c Z","P 42/n c m S","C 42/a m c S"]
sg_std[139,0:2] = ["I 4/m m m","F 4/m m m"]
sg_std[140,0:2] = ["I 4/m c m","F 4/m m c"]
sg_std[141,0:6] = ["I 41/a m d","F 41/d d m","I 41/a m d Z","F 41/d d m Z","I 41/a m d S","F 41/d d m S"]
sg_std[142,0:7] = ["I 41/a c d","F 41/d d c","I 41/a c d Z","F 41/d d c Z","I 41/a c d S","F 41/d d c S",
                   "F 41/a d c"]

#Trigonal
sg_std[143,0:2] = ["P 3","H 3"]
sg_std[144,0:2] = ["P 31","H 31"]
sg_std[145,0:2] = ["P 32","H 32"]
sg_std[146,0:3] = ["R 3","R 3 R","R 3 H"]
sg_std[147,0:2] = ["P -3","H -3"]
sg_std[148,0:3] = ["R -3","R -3 H","R -3 R"] 
sg_std[149,0:2] = ["P 3 1 2","H 3 2 1"]
sg_std[150,0:2] = ["P 3 2 1","H 3 1 2"]
sg_std[151,0:2] = ["P 31 1 2","H 31 2 1"]
sg_std[152,0:2] = ["P 31 2 1","H 31 1 2"]
sg_std[153,0:2] = ["P 32 1 2","H 32 2 1"]
sg_std[154,0:2] = ["P 32 2 1","H 32 1 2"]
sg_std[155,0:3] = ["R 3 2","R 3 2 R","R 3 2 H"]
sg_std[156,0:2] = ["P 3 m 1","H 3 1 m"]
sg_std[157,0:2] = ["P 3 1 m","H 3 m 1"]
sg_std[158,0:2] = ["P 3 c 1","H 3 1 c"]
sg_std[159,0:2] = ["P 3 1 c","H 3 c 1"]
sg_std[160,0:4] = ["R 3 m","R 3 m R","R 3 m H","R 3 m HR"]
sg_std[161,0:3] = ["R 3 c","R 3 c R","R 3 c H"]
sg_std[162,0:2] = ["P -3 1 m","H -3 m 1"]
sg_std[163,0:2] = ["P -3 1 c","H -3 c 1"]
sg_std[164,0:2] = ["P -3 m 1","H -3 1 m"]
sg_std[165,0:6] = ["P -3 c 1","H -3 1 c","P -3 c 1 H","H -3 1 c H","P -3 c 1 R","H -3 1 c R"]
sg_std[166,0:4] = ["R -3 m","R -3 m R","R -3 m H","R -3 m HR"]
sg_std[167,0:3] = ["R -3 c","R -3 c R","R -3 c H"] 

#Hexagonal
sg_std[168,0:1] = ["P 6"] 
sg_std[169,0:1] = ["P 61"] 
sg_std[170,0:1] = ["P 65"] 
sg_std[171,0:1] = ["P 62"] 
sg_std[172,0:1] = ["P 64"] 
sg_std[173,0:1] = ["P 63"] 
sg_std[174,0:1] = ["P -6"] 
sg_std[175,0:1] = ["P 6/m"] 
sg_std[176,0:1] = ["P 63/m"] 
sg_std[177,0:1] = ["P 6 2 2"] 
sg_std[178,0:1] = ["P 61 2 2"] 
sg_std[179,0:1] = ["P 65 2 2"] 
sg_std[180,0:1] = ["P 62 2 2"] 
sg_std[181,0:1] = ["P 64 2 2"] 
sg_std[182,0:1] = ["P 63 2 2"] 
sg_std[183,0:1] = ["P 6 m m"]
sg_std[184,0:1] = ["P 6 c c"] 
sg_std[185,0:1] = ["P 63 c m"]
sg_std[186,0:1] = ["P 63 m c"]
sg_std[187,0:1] = ["P -6 m 2"] 
sg_std[188,0:1] = ["P -6 c 2"] 
sg_std[189,0:1] = ["P -6 2 m"] 
sg_std[190,0:1] = ["P -6 2 c"] 
sg_std[191,0:1] = ["P 6/m m m"]
sg_std[192,0:1] = ["P 6/m c c"] 
sg_std[193,0:1] = ["P 63/m c m"] 
sg_std[194,0:1] = ["P 63/m m c"] 

#Cubic
sg_std[195,0:1] = ["P 2 3"]
sg_std[196,0:1] = ["F 2 3"]
sg_std[197,0:1] = ["I 2 3"]
sg_std[198,0:1] = ["P 21 3"]
sg_std[199,0:1] = ["I 21 3"]
sg_std[200,0:1] = ["P m -3"]
sg_std[201,0:3] = ["P n -3","P n -3 Z","P n -3 S"]
sg_std[202,0:1] = ["F m -3"]
sg_std[203,0:3] = ["F d -3","F d -3 Z","F d -3 S"]
sg_std[204,0:1] = ["I m -3"]
sg_std[205,0:1] = ["P a -3"]
sg_std[206,0:1] = ["I a -3"]
sg_std[207,0:1] = ["P 4 3 2"]
sg_std[208,0:1] = ["P 42 3 2"]
sg_std[209,0:1] = ["F 4 3 2"]
sg_std[210,0:1] = ["F 41 3 2"]
sg_std[211,0:1] = ["I 4 3 2"]
sg_std[212,0:1] = ["P 43 3 2"]
sg_std[213,0:1] = ["P 41 3 2"]
sg_std[214,0:1] = ["I 41 3 2"]
sg_std[215,0:1] = ["P -4 3 m"]
sg_std[216,0:1] = ["F -4 3 m"]
sg_std[217,0:1] = ["I -4 3 m"]
sg_std[218,0:1] = ["P -4 3 n"]
sg_std[219,0:1] = ["F -4 3 c"]
sg_std[220,0:1] = ["I -4 3 d"]
sg_std[221,0:1] = ["P m -3 m"]
sg_std[222,0:3] = ["P n -3 n","P n -3 n Z","P n -3 n S"]
sg_std[223,0:1] = ["P m -3 n"]
sg_std[224,0:3] = ["P n -3 m","P n -3 m Z","P n -3 m S"]
sg_std[225,0:1] = ["F m -3 m"]
sg_std[226,0:1] = ["F m -3 c"]
sg_std[227,0:3] = ["F d -3 m","F d -3 m Z","F d -3 m S"]
sg_std[228,0:3] = ["F d -3 c","F d -3 c Z","F d -3 c S"]
sg_std[229,0:1] = ["I m -3 m"]
sg_std[230,0:1] = ["I a -3 d"]

# Space Group in ICSD CIF

sg_cif = np.empty((231, 14), dtype=object)

#Triclnic
sg_cif[1,0:5] = ["P 1","B 1","C 1","F 1","I 1"]
sg_cif[2,0:6] = ["P -1","A -1", "B -1","C -1","F -1","I -1"]

#Monoclinic
sg_cif[3,0:2] = ["P 1 2 1","P 1 1 2"]
sg_cif[4,0:5] = ["P 1 21 1","B 1 21 1","P 1 1 21","C 1 1 21","P 21 1 1"]
sg_cif[5,0:9] = ["C 1 2 1","A 1 2 1","I 1 2 1","F 1 2 1","A 1 1 2","B 1 1 2","I 1 1 2","F 1 1 2","C 2 1 1"]
sg_cif[6,0:3] = ["P 1 m 1","P 1 1 m","P m 1 1"]
sg_cif[7,0:9] = ["P 1 c 1","P 1 a 1","P 1 n 1","B 1 a 1","P 1 1 a","P 1 1 b","P 1 1 n","P c 1 1","P n 1 1"]
sg_cif[8,0:8] = ["C 1 m 1","A 1 m 1","I 1 m 1","A 1 1 m","B 1 1 m","I 1 1 m","B m 1 1","F m 1 1"]
sg_cif[9,0:10] = ["C 1 c 1","A 1 n 1","I 1 a 1","A 1 a 1","I 1 c 1","A 1 1 a","I 1 1 b","B 1 1 b","F d 1 1","F 1 d 1"]
sg_cif[10,0:4] = ["P 1 2/m 1","P 1 1 2/m","C 1 1 2/m","P 2/m 1 1"]
sg_cif[11,0:5] = ["P 1 21/m 1","B 1 21/m 1","P 1 1 21/m","C 1 1 21/m","P 21/m 1 1"]
sg_cif[12,0:11] = ["C 1 2/m 1","A 1 2/m 1","I 1 2/m 1","F 1 2/m 1","A 1 1 2/m","B 1 1 2/m",
                   "I 1 1 2/m","F 1 1 2/m","B 2/m 1 1","C 2/m 1 1","I 2/m 1 1"]
sg_cif[13,0:9] = ["P 1 2/c 1","P 1 2/a 1","P 1 2/n 1","P 1 1 2/a","P 1 1 2/b","P 1 1 2/n",
                  "C 1 1 2/a","P 2/c 1 1","B 1 2/c 1"]
sg_cif[14,0:14] = ["P 1 21/c 1","P 1 21/n 1","P 1 21/a 1","P 1 1 21/a","P 1 1 21/n","P 1 1 21/b",
                   "P 21/b 1 1","P 21/n 1 1","P 21/c 1 1","B 1 21/a 1","B 1 21/d 1","C 1 1 21/d",
                   "A 21/d 1 1","B 1 21/c 1"]
sg_cif[15,0:14] = ["C 1 2/c 1","A 1 2/n 1","I 1 2/a 1","A 1 2/a 1","C 1 2/n 1","I 1 2/c 1",
                   "A 1 1 2/a","B 1 1 2/n","I 1 1 2/b","B 1 1 2/b","I 1 1 2/a","F 1 2/d 1",
                   "A 1 2/a 1 S","I 1 1 2/a S"]

#Orthorhombic
sg_cif[16,0:1] = ["P 2 2 2"] 
sg_cif[17,0:3] = ["P 2 2 21","P 2 21 2","P 21 2 2"] 
sg_cif[18,0:3] = ["P 21 21 2","P 21 2 21","P 2 21 21"] 
sg_cif[19,0:1] = ["P 21 21 21"] 
sg_cif[20,0:4] = ["C 2 2 21","B 2 21 2","A 21 2 2","C 2 2 21 S"]
sg_cif[21,0:2] = ["C 2 2 2","A 2 2 2"] 
sg_cif[22,0:1] = ["F 2 2 2"] 
sg_cif[23,0:1] = ["I 2 2 2"] 
sg_cif[24,0:1] = ["I 21 21 21"] 
sg_cif[25,0:3] = ["P m m 2","P m 2 m","P 2 m m"] 
sg_cif[26,0:6] = ["P m c 21","P c m 21","P b 21 m","P m 21 b","P 21 m a","P 21 a m"]
sg_cif[27,0:1] = ["P c c 2"] 
sg_cif[28,0:4] = ["P m a 2","P b m 2","P m 2 a","P 2 c m"]
sg_cif[29,0:6] = ["P c a 21","P b c 21","P c 21 b","P b 21 a","P 21 a b","P 21 c a"]
sg_cif[30,0:4] = ["P n c 2","P c n 2","P b 2 n","P 2 a n"]
sg_cif[31,0:6] = ["P m n 21","P n m 21","P n 21 m","P m 21 n","P 21 m n","P 21 n m"]
sg_cif[32,0:1] = ["P b a 2"] 
sg_cif[33,0:6] = ["P n a 21","P b n 21","P c 21 n","P n 21 a","P 21 n b","P 21 c n"]
sg_cif[34,0:3] = ["P n n 2","P n 2 n","P 2 n n"] 
sg_cif[35,0:2] = ["C m m 2","A 2 m m"] 
sg_cif[36,0:6] = ["C m c 21","C c m 21","B b 21 m","B m 21 b","A 21 m a","A 21 a m"]
sg_cif[37,0:3] = ["C c c 2","B b 2 b","A 2 a a"] 
sg_cif[38,0:6] = ["A m m 2","B m m 2","C m 2 m","A m 2 m","B 2 m m","C 2 m m"]
sg_cif[39,0:3] = ["A b m 2","C m 2 a","C 2 m b"]
sg_cif[40,0:5] = ["A m a 2","B b m 2","C c 2 m","B 2 m b","C 2 c m"]
sg_cif[41,0:5] = ["A b a 2","B b a 2","C c 2 a","B 2 c b","C 2 c b"]
sg_cif[42,0:3] = ["F m m 2","F 2 m m","F m 2 m"] 
sg_cif[43,0:3] = ["F d d 2","F d 2 d","F 2 d d"] 
sg_cif[44,0:3] = ["I m m 2","I m 2 m","I 2 m m"] 
sg_cif[45,0:1] = ["I b a 2"] 
sg_cif[46,0:6] = ["I m a 2","I b m 2","I 2 a m","I 2 m b","I 2 c m","I c 2 m"]
sg_cif[47,0:1] = ["P m m m"] 
sg_cif[48,0:2] = ["P n n n","P n n n S"] 
sg_cif[49,0:1] = ["P c c m"] 
sg_cif[50,0:2] = ["P b a n","P b a n S"]
sg_cif[51,0:5] = ["P m m a","P m m b","P m c m","P m a m","P b m m"]
sg_cif[52,0:6] = ["P n n a","P n c n","P n a n","P b n n","P c n n","P n a n S"]
sg_cif[53,0:6] = ["P m n a","P n m b","P n c m","P m a n","P b m n","P c n m"]
sg_cif[54,0:5] = ["P c c a","P c c b","P b c b","P b a b","P b a a"]
sg_cif[55,0:3] = ["P b a m","P c m a","P m c b"] 
sg_cif[56,0:3] = ["P c c n","P b n b","P n a a"] 
sg_cif[57,0:6] = ["P b c m","P c a m","P b m a","P c m b","P m c a","P m a b"]
sg_cif[58,0:3] = ["P n n m","P n m n","P m n n"] 
sg_cif[59,0:6] = ["P m m n","P m n m","P n m m","P m m n S","P m n m S","P n m m S"] 
sg_cif[60,0:6] = ["P b c n","P c a n","P b n a","P c n b","P n c a","P n a b"]
sg_cif[61,0:2] = ["P b c a","P c a b"] 
sg_cif[62,0:6] = ["P n m a","P n a m","P m c n","P c m n","P b n m","P m n b"]
sg_cif[63,0:6] = ["C m c m","C c m m","B b m m","B m m b","A m m a","A m a m"]
sg_cif[64,0:7] = ["C m c a","A b m a","A b a m","B m a b","C c m b","A c a m","B b c m"]
sg_cif[65,0:3] = ["C m m m","A m m m","B m m m"] 
sg_cif[66,0:3] = ["C c c m","B b m b","A m a a"] 
sg_cif[67,0:4] = ["C m m a","A b m m","A c m m","B m c m"] 
sg_cif[68,0:7] = ["C c c a","B b a b","C c c a S","C c c e","C c c e S","B b c b", "A c a a"] 
sg_cif[69,0:1] = ["F m m m"] 
sg_cif[70,0:2] = ["F d d d","F d d d S"] 
sg_cif[71,0:1] = ["I m m m"] 
sg_cif[72,0:3] = ["I b a m","I m c b","I c m a"] 
sg_cif[73,0:1] = ["I b c a"] 
sg_cif[74,0:6] = ["I m m a","I m m b","I b m m","I c m m","I m c m","I m a m"] 

#Tetragonal
sg_cif[75,0:1] = ["P 4"]
sg_cif[76,0:1] = ["P 41"]
sg_cif[77,0:1] = ["P 42"]
sg_cif[78,0:1] = ["P 43"]
sg_cif[79,0:1] = ["I 4"]
sg_cif[80,0:1] = ["I 41"]
sg_cif[81,0:1] = ["P -4"]
sg_cif[82,0:1] = ["I -4"]
sg_cif[83,0:1] = ["P 4/m"]
sg_cif[84,0:1] = ["P 42/m"]
sg_cif[85,0:2] = ["P 4/n","P 4/n S"]
sg_cif[86,0:2] = ["P 42/n","P 42/n S"]
sg_cif[87,0:2] = ["I 4/m","F 4/m"]
sg_cif[88,0:2] = ["I 41/a","I 41/a S"]
sg_cif[89,0:1] = ["P 4 2 2"]
sg_cif[90,0:2] = ["P 4 21 2","C 4 2 21"]
sg_cif[91,0:1] = ["P 41 2 2"]
sg_cif[92,0:1] = ["P 41 21 2"]
sg_cif[93,0:1] = ["P 42 2 2"]
sg_cif[94,0:1] = ["P 42 21 2"]
sg_cif[95,0:1] = ["P 43 2 2"]
sg_cif[96,0:1] = ["P 43 21 2"]
sg_cif[97,0:1] = ["I 4 2 2"]
sg_cif[98,0:1] = ["I 41 2 2"]
sg_cif[99,0:1] = ["P 4 m m"]
sg_cif[100,0:1] = ["P 4 b m"]
sg_cif[101,0:1] = ["P 42 c m"]
sg_cif[102,0:1] = ["P 42 n m"]
sg_cif[103,0:1] = ["P 4 c c"]
sg_cif[104,0:1] = ["P 4 n c"]
sg_cif[105,0:1] = ["P 42 m c"]
sg_cif[106,0:1] = ["P 42 b c"]
sg_cif[107,0:1] = ["I 4 m m"]
sg_cif[108,0:1] = ["I 4 c m"]
sg_cif[109,0:1] = ["I 41 m d"]
sg_cif[110,0:1] = ["I 41 c d"]
sg_cif[111,0:1] = ["P -4 2 m"]
sg_cif[112,0:1] = ["P -4 2 c"]
sg_cif[113,0:2] = ["P -4 21 m","C -4 m 21"]
sg_cif[114,0:1] = ["P -4 21 c"]
sg_cif[115,0:1] = ["P -4 m 2"]
sg_cif[116,0:1] = ["P -4 c 2"]
sg_cif[117,0:2] = ["P -4 b 2","C -4 2 b"]
sg_cif[118,0:1] = ["P -4 n 2"]
sg_cif[119,0:1] = ["I -4 m 2"]
sg_cif[120,0:1] = ["I -4 c 2"]
sg_cif[121,0:1] = ["I -4 2 m"]
sg_cif[122,0:2] = ["I -4 2 d","F -4 d 2"]
sg_cif[123,0:1] = ["P 4/m m m"]
sg_cif[124,0:2] = ["P 4/m c c","C 4/m c c"]
sg_cif[125,0:2] = ["P 4/n b m","P 4/n b m S"]
sg_cif[126,0:2] = ["P 4/n n c","P 4/n n c S"]
sg_cif[127,0:1] = ["P 4/m b m"]
sg_cif[128,0:1] = ["P 4/m n c"]
sg_cif[129,0:2] = ["P 4/n m m","P 4/n m m S"]
sg_cif[130,0:2] = ["P 4/n c c","P 4/n c c S"]
sg_cif[131,0:1] = ["P 42/m m c"]
sg_cif[132,0:1] = ["P 42/m c m"]
sg_cif[133,0:2] = ["P 42/n b c","P 42/n b c S"]
sg_cif[134,0:2] = ["P 42/n n m","P 42/n n m S"]
sg_cif[135,0:1] = ["P 42/m b c"]
sg_cif[136,0:1] = ["P 42/m n m"]
sg_cif[137,0:2] = ["P 42/n m c","P 42/n m c S"]
sg_cif[138,0:2] = ["P 42/n c m","P 42/n c m S"]
sg_cif[139,0:2] = ["I 4/m m m","F 4/m m m"]
sg_cif[140,0:2] = ["I 4/m c m","F 4/m m c"]
sg_cif[141,0:3] = ["I 41/a m d","F 41/d d m","I 41/a m d S"]
sg_cif[142,0:3] = ["I 41/a c d","I 41/a c d S","F 41/a d c"]

#Trigonal
sg_cif[143,0:1] = ["P 3"]
sg_cif[144,0:1] = ["P 31"]
sg_cif[145,0:1] = ["P 32"]
sg_cif[146,0:2] = ["R 3","R 3 R"]
sg_cif[147,0:1] = ["P -3"]
sg_cif[148,0:2] = ["R -3","R -3 R"] 
sg_cif[149,0:1] = ["P 3 1 2"]
sg_cif[150,0:1] = ["P 3 2 1"]
sg_cif[151,0:1] = ["P 31 1 2"]
sg_cif[152,0:1] = ["P 31 2 1"]
sg_cif[153,0:1] = ["P 32 1 2"]
sg_cif[154,0:1] = ["P 32 2 1"]
sg_cif[155,0:2] = ["R 3 2","R 3 2 R"]
sg_cif[156,0:1] = ["P 3 m 1"]
sg_cif[157,0:1] = ["P 3 1 m"]
sg_cif[158,0:1] = ["P 3 c 1"]
sg_cif[159,0:1] = ["P 3 1 c"]
sg_cif[160,0:2] = ["R 3 m","R 3 m R"]
sg_cif[161,0:2] = ["R 3 c","R 3 c R"]
sg_cif[162,0:1] = ["P -3 1 m"]
sg_cif[163,0:1] = ["P -3 1 c"]
sg_cif[164,0:1] = ["P -3 m 1"]
sg_cif[165,0:1] = ["P -3 c 1"]
sg_cif[166,0:2] = ["R -3 m","R -3 m R"]
sg_cif[167,0:2] = ["R -3 c","R -3 c R"] 

#Hexagonal
sg_cif[168,0:1] = ["P 6"] 
sg_cif[169,0:1] = ["P 61"] 
sg_cif[170,0:1] = ["P 65"] 
sg_cif[171,0:1] = ["P 62"] 
sg_cif[172,0:1] = ["P 64"] 
sg_cif[173,0:1] = ["P 63"] 
sg_cif[174,0:1] = ["P -6"] 
sg_cif[175,0:1] = ["P 6/m"] 
sg_cif[176,0:1] = ["P 63/m"] 
sg_cif[177,0:1] = ["P 6 2 2"] 
sg_cif[178,0:1] = ["P 61 2 2"] 
sg_cif[179,0:1] = ["P 65 2 2"] 
sg_cif[180,0:1] = ["P 62 2 2"] 
sg_cif[181,0:1] = ["P 64 2 2"] 
sg_cif[182,0:1] = ["P 63 2 2"] 
sg_cif[183,0:1] = ["P 6 m m"]
sg_cif[184,0:1] = ["P 6 c c"] 
sg_cif[185,0:1] = ["P 63 c m"]
sg_cif[186,0:1] = ["P 63 m c"]
sg_cif[187,0:1] = ["P -6 m 2"] 
sg_cif[188,0:1] = ["P -6 c 2"] 
sg_cif[189,0:1] = ["P -6 2 m"] 
sg_cif[190,0:1] = ["P -6 2 c"] 
sg_cif[191,0:1] = ["P 6/m m m"]
sg_cif[192,0:1] = ["P 6/m c c"] 
sg_cif[193,0:1] = ["P 63/m c m"] 
sg_cif[194,0:1] = ["P 63/m m c"] 

#Cubic
sg_cif[195,0:1] = ["P 2 3"]
sg_cif[196,0:1] = ["F 2 3"]
sg_cif[197,0:1] = ["I 2 3"]
sg_cif[198,0:1] = ["P 21 3"]
sg_cif[199,0:1] = ["I 21 3"]
sg_cif[200,0:1] = ["P m -3"]
sg_cif[201,0:2] = ["P n -3","P n -3 S"]
sg_cif[202,0:1] = ["F m -3"]
sg_cif[203,0:2] = ["F d -3","F d -3 S"]
sg_cif[204,0:1] = ["I m -3"]
sg_cif[205,0:1] = ["P a -3"]
sg_cif[206,0:1] = ["I a -3"]
sg_cif[207,0:1] = ["P 4 3 2"]
sg_cif[208,0:1] = ["P 42 3 2"]
sg_cif[209,0:1] = ["F 4 3 2"]
sg_cif[210,0:1] = ["F 41 3 2"]
sg_cif[211,0:1] = ["I 4 3 2"]
sg_cif[212,0:1] = ["P 43 3 2"]
sg_cif[213,0:1] = ["P 41 3 2"]
sg_cif[214,0:1] = ["I 41 3 2"]
sg_cif[215,0:1] = ["P -4 3 m"]
sg_cif[216,0:1] = ["F -4 3 m"]
sg_cif[217,0:1] = ["I -4 3 m"]
sg_cif[218,0:1] = ["P -4 3 n"]
sg_cif[219,0:1] = ["F -4 3 c"]
sg_cif[220,0:1] = ["I -4 3 d"]
sg_cif[221,0:1] = ["P m -3 m"]
sg_cif[222,0:1] = ["P n -3 n"]
sg_cif[223,0:1] = ["P m -3 n"]
sg_cif[224,0:2] = ["P n -3 m","P n -3 m S"]
sg_cif[225,0:1] = ["F m -3 m"]
sg_cif[226,0:1] = ["F m -3 c"]
sg_cif[227,0:2] = ["F d -3 m","F d -3 m S"]
sg_cif[228,0:1] = ["F d -3 c"]
sg_cif[229,0:1] = ["I m -3 m"]
sg_cif[230,0:1] = ["I a -3 d"]

# Space Group for Fullptof

sg_fp = np.empty((231, 11), dtype=object)

#Triclnic
sg_fp[1,0:5] = ["P 1","B 1","C 1","F 1","I 1"]
sg_fp[2,0:6] = ["P -1","A -1", "B -1","C -1","F -1","I -1"]

#Monoclinic
sg_fp[3,0:2] = ["P 1 2 1","P 1 1 2"]
sg_fp[4,0:3] = ["P 1 21 1","P 1 1 21","P 21 1 1"]
sg_fp[5,0:7] = ["C 1 2 1","A 1 2 1","I 1 2 1","A 1 1 2","B 1 1 2","I 1 1 2","C 2 1 1"]
sg_fp[6,0:3] = ["P 1 m 1","P 1 1 m","P m 1 1"]
sg_fp[7,0:8] = ["P 1 c 1","P 1 a 1","P 1 n 1","P 1 1 a","P 1 1 b","P 1 1 n","P c 1 1","P n 1 1"]
sg_fp[8,0:7] = ["C 1 m 1","A 1 m 1","I 1 m 1","A 1 1 m","B 1 1 m","I 1 1 m","B m 1 1"]
sg_fp[9,0:8] = ["C 1 c 1","A 1 n 1","I 1 a 1","A 1 a 1","I 1 c 1","A 1 1 a","I 1 1 b","B 1 1 b"]
sg_fp[10,0:3] = ["P 1 2/m 1","P 1 1 2/m","P 2/m 1 1"]
sg_fp[11,0:4] = ["P 1 21/m 1","B 1 21/m 1","P 1 1 21/m","P 21/m 1 1"]
sg_fp[12,0:10] = ["C 1 2/m 1","A 1 2/m 1","I 1 2/m 1","F 1 2/m 1","A 1 1 2/m","B 1 1 2/m",
                   "I 1 1 2/m","B 2/m 1 1","C 2/m 1 1","I 2/m 1 1"]
sg_fp[13,0:8] = ["P 1 2/c 1","P 1 2/a 1","P 1 2/n 1","P 1 1 2/a","P 1 1 2/b","P 1 1 2/n","C 1 1 2/a","P 2/c 1 1"]
sg_fp[14,0:10] = ["P 1 21/c 1","P 1 21/n 1","P 1 21/a 1","P 1 1 21/a","P 1 1 21/n","P 1 1 21/b",
                   "P 21/b 1 1","P 21/n 1 1","P 21/c 1 1","B 1 21/c 1"]
sg_fp[15,0:11] = ["C 1 2/c 1","A 1 2/n 1","I 1 2/a 1","A 1 2/a 1","C 1 2/n 1","I 1 2/c 1",
                   "A 1 1 2/a","B 1 1 2/n","I 1 1 2/b","B 1 1 2/b","I 1 1 2/a"]

#Orthorhombic
sg_fp[16,0:1] = ["P 2 2 2"] 
sg_fp[17,0:3] = ["P 2 2 21","P 2 21 2","P 21 2 2"] 
sg_fp[18,0:3] = ["P 21 21 2","P 21 2 21","P 2 21 21"] 
sg_fp[19,0:1] = ["P 21 21 21"] 
sg_fp[20,0:3] = ["C 2 2 21","B 2 21 2","A 21 2 2"]
sg_fp[21,0:2] = ["C 2 2 2","A 2 2 2"] 
sg_fp[22,0:1] = ["F 2 2 2"] 
sg_fp[23,0:1] = ["I 2 2 2"] 
sg_fp[24,0:1] = ["I 21 21 21"] 
sg_fp[25,0:3] = ["P m m 2","P m 2 m","P 2 m m"] 
sg_fp[26,0:6] = ["P m c 21","P c m 21","P b 21 m","P m 21 b","P 21 m a","P 21 a m"]
sg_fp[27,0:1] = ["P c c 2"] 
sg_fp[28,0:4] = ["P m a 2","P b m 2","P m 2 a","P 2 c m"]
sg_fp[29,0:6] = ["P c a 21","P b c 21","P c 21 b","P b 21 a","P 21 a b","P 21 c a"]
sg_fp[30,0:4] = ["P n c 2","P c n 2","P b 2 n","P 2 a n"]
sg_fp[31,0:6] = ["P m n 21","P n m 21","P n 21 m","P m 21 n","P 21 m n","P 21 n m"]
sg_fp[32,0:1] = ["P b a 2"] 
sg_fp[33,0:6] = ["P n a 21","P b n 21","P c 21 n","P n 21 a","P 21 n b","P 21 c n"]
sg_fp[34,0:3] = ["P n n 2","P n 2 n","P 2 n n"] 
sg_fp[35,0:2] = ["C m m 2","A 2 m m"] 
sg_fp[36,0:6] = ["C m c 21","C c m 21","B b 21 m","B m 21 b","A 21 m a","A 21 a m"]
sg_fp[37,0:3] = ["C c c 2","B b 2 b","A 2 a a"] 
sg_fp[38,0:6] = ["A m m 2","B m m 2","C m 2 m","A m 2 m","B 2 m m","C 2 m m"]
sg_fp[39,0:3] = ["A b m 2","C m 2 a","C 2 m b"]
sg_fp[40,0:5] = ["A m a 2","B b m 2","C c 2 m","B 2 m b","C 2 c m"]
sg_fp[41,0:5] = ["A b a 2","B b a 2","C c 2 a","B 2 c b","C 2 c b"]
sg_fp[42,0:3] = ["F m m 2","F 2 m m","F m 2 m"] 
sg_fp[43,0:3] = ["F d d 2","F d 2 d","F 2 d d"] 
sg_fp[44,0:3] = ["I m m 2","I m 2 m","I 2 m m"]
sg_fp[45,0:1] = ["I b a 2"]
sg_fp[46,0:5] = ["I m a 2","I b m 2","I 2 m b","I 2 c m","I c 2 m"]
sg_fp[47,0:1] = ["P m m m"]
sg_fp[48,0:1] = ["P n n n"]
sg_fp[49,0:1] = ["P c c m"]
sg_fp[50,0:1] = ["P b a n"]
sg_fp[51,0:5] = ["P m m a","P m m b","P m c m","P m a m","P b m m"]
sg_fp[52,0:5] = ["P n n a","P n c n","P n a n","P b n n","P c n n"]
sg_fp[53,0:6] = ["P m n a","P n m b","P n c m","P m a n","P b m n","P c n m"]
sg_fp[54,0:5] = ["P c c a","P c c b","P b c b","P b a b","P b a a"]
sg_fp[55,0:3] = ["P b a m","P c m a","P m c b"] 
sg_fp[56,0:3] = ["P c c n","P b n b","P n a a"] 
sg_fp[57,0:6] = ["P b c m","P c a m","P b m a","P c m b","P m c a","P m a b"]
sg_fp[58,0:3] = ["P n n m","P n m n","P m n n"] 
sg_fp[59,0:3] = ["P m m n","P m n m","P n m m"] 
sg_fp[60,0:6] = ["P b c n","P c a n","P b n a","P c n b","P n c a","P n a b"]
sg_fp[61,0:2] = ["P b c a","P c a b"] 
sg_fp[62,0:6] = ["P n m a","P n a m","P m c n","P c m n","P b n m","P m n b"]
sg_fp[63,0:6] = ["C m c m","C c m m","B b m m","B m m b","A m m a","A m a m"]
sg_fp[64,0:6] = ["C m c a","A b m a","B m a b","C c m b","A c a m","B b c m"]
sg_fp[65,0:3] = ["C m m m","A m m m","B m m m"] 
sg_fp[66,0:2] = ["C c c m","A m a a"] 
sg_fp[67,0:4] = ["C m m a","A b m m","A c m m","B m c m"] 
sg_fp[68,0:4] = ["C c c a","B b a b","B b c b","A c a a"] 
sg_fp[69,0:1] = ["F m m m"] 
sg_fp[70,0:1] = ["F d d d"] 
sg_fp[71,0:1] = ["I m m m"] 
sg_fp[72,0:3] = ["I b a m","I m c b","I c m a"] 
sg_fp[73,0:1] = ["I b c a"] 
sg_fp[74,0:6] = ["I m m a","I m m b","I b m m","I c m m","I m c m","I m a m"] 

#Tetragonal
sg_fp[75,0:1] = ["P 4"]
sg_fp[76,0:1] = ["P 41"]
sg_fp[77,0:1] = ["P 42"]
sg_fp[78,0:1] = ["P 43"]
sg_fp[79,0:1] = ["I 4"]
sg_fp[80,0:1] = ["I 41"]
sg_fp[81,0:1] = ["P -4"]
sg_fp[82,0:1] = ["I -4"]
sg_fp[83,0:1] = ["P 4/m"]
sg_fp[84,0:1] = ["P 42/m"]
sg_fp[85,0:1] = ["P 4/n"]
sg_fp[86,0:1] = ["P 42/n"]
sg_fp[87,0:1] = ["I 4/m"]
sg_fp[88,0:1] = ["I 41/a"]
sg_fp[89,0:1] = ["P 4 2 2"]
sg_fp[90,0:2] = ["P 4 21 2","C 4 2 21"]
sg_fp[91,0:1] = ["P 41 2 2"]
sg_fp[92,0:1] = ["P 41 21 2"]
sg_fp[93,0:1] = ["P 42 2 2"]
sg_fp[94,0:1] = ["P 42 21 2"]
sg_fp[95,0:1] = ["P 43 2 2"]
sg_fp[96,0:1] = ["P 43 21 2"]
sg_fp[97,0:1] = ["I 4 2 2"]
sg_fp[98,0:1] = ["I 41 2 2"]
sg_fp[99,0:1] = ["P 4 m m"]
sg_fp[100,0:1] = ["P 4 b m"]
sg_fp[101,0:1] = ["P 42 c m"]
sg_fp[102,0:1] = ["P 42 n m"]
sg_fp[103,0:1] = ["P 4 c c"]
sg_fp[104,0:1] = ["P 4 n c"]
sg_fp[105,0:1] = ["P 42 m c"]
sg_fp[106,0:1] = ["P 42 b c"]
sg_fp[107,0:1] = ["I 4 m m"]
sg_fp[108,0:1] = ["I 4 c m"]
sg_fp[109,0:1] = ["I 41 m d"]
sg_fp[110,0:1] = ["I 41 c d"]
sg_fp[111,0:1] = ["P -4 2 m"]
sg_fp[112,0:1] = ["P -4 2 c"]
sg_fp[113,0:1] = ["P -4 21 m"]
sg_fp[114,0:1] = ["P -4 21 c"]
sg_fp[115,0:1] = ["P -4 m 2"]
sg_fp[116,0:1] = ["P -4 c 2"]
sg_fp[117,0:1] = ["P -4 b 2"]
sg_fp[118,0:1] = ["P -4 n 2"]
sg_fp[119,0:1] = ["I -4 m 2"]
sg_fp[120,0:1] = ["I -4 c 2"]
sg_fp[121,0:1] = ["I -4 2 m"]
sg_fp[122,0:2] = ["I -4 2 d","F -4 d 2"]
sg_fp[123,0:1] = ["P 4/m m m"]
sg_fp[124,0:1] = ["P 4/m c c"]
sg_fp[125,0:1] = ["P 4/n b m"]
sg_fp[126,0:1] = ["P 4/n n c"]
sg_fp[127,0:1] = ["P 4/m b m"]
sg_fp[128,0:1] = ["P 4/m n c"]
sg_fp[129,0:1] = ["P 4/n m m"]
sg_fp[130,0:1] = ["P 4/n c c"]
sg_fp[131,0:1] = ["P 42/m m c"]
sg_fp[132,0:1] = ["P 42/m c m"]
sg_fp[133,0:1] = ["P 42/n b c"]
sg_fp[134,0:1] = ["P 42/n n m"]
sg_fp[135,0:1] = ["P 42/m b c"]
sg_fp[136,0:1] = ["P 42/m n m"]
sg_fp[137,0:1] = ["P 42/n m c"]
sg_fp[138,0:1] = ["P 42/n c m"]
sg_fp[139,0:2] = ["I 4/m m m","F 4/m m m"]
sg_fp[140,0:1] = ["I 4/m c m"]
sg_fp[141,0:1] = ["I 41/a m d"]
sg_fp[142,0:1] = ["I 41/a c d"]

#Trigonal
sg_fp[143,0:1] = ["P 3"]
sg_fp[144,0:1] = ["P 31"]
sg_fp[145,0:1] = ["P 32"]
sg_fp[146,0:1] = ["R 3"]
sg_fp[147,0:1] = ["P -3"]
sg_fp[148,0:1] = ["R -3"] 
sg_fp[149,0:1] = ["P 3 1 2"]
sg_fp[150,0:1] = ["P 3 2 1"]
sg_fp[151,0:1] = ["P 31 1 2"]
sg_fp[152,0:1] = ["P 31 2 1"]
sg_fp[153,0:1] = ["P 32 1 2"]
sg_fp[154,0:1] = ["P 32 2 1"]
sg_fp[155,0:1] = ["R 3 2"]
sg_fp[156,0:1] = ["P 3 m 1"]
sg_fp[157,0:1] = ["P 3 1 m"]
sg_fp[158,0:1] = ["P 3 c 1"]
sg_fp[159,0:1] = ["P 3 1 c"]
sg_fp[160,0:1] = ["R 3 m"]
sg_fp[161,0:1] = ["R 3 c"]
sg_fp[162,0:1] = ["P -3 1 m"]
sg_fp[163,0:1] = ["P -3 1 c"]
sg_fp[164,0:1] = ["P -3 m 1"]
sg_fp[165,0:1] = ["P -3 c 1"]
sg_fp[166,0:1] = ["R -3 m"]
sg_fp[167,0:1] = ["R -3 c"] 

#Hexagonal
sg_fp[168,0:1] = ["P 6"] 
sg_fp[169,0:1] = ["P 61"] 
sg_fp[170,0:1] = ["P 65"] 
sg_fp[171,0:1] = ["P 62"] 
sg_fp[172,0:1] = ["P 64"] 
sg_fp[173,0:1] = ["P 63"] 
sg_fp[174,0:1] = ["P -6"] 
sg_fp[175,0:1] = ["P 6/m"] 
sg_fp[176,0:1] = ["P 63/m"] 
sg_fp[177,0:1] = ["P 6 2 2"] 
sg_fp[178,0:1] = ["P 61 2 2"] 
sg_fp[179,0:1] = ["P 65 2 2"] 
sg_fp[180,0:1] = ["P 62 2 2"] 
sg_fp[181,0:1] = ["P 64 2 2"] 
sg_fp[182,0:1] = ["P 63 2 2"] 
sg_fp[183,0:1] = ["P 6 m m"]
sg_fp[184,0:1] = ["P 6 c c"] 
sg_fp[185,0:1] = ["P 63 c m"]
sg_fp[186,0:1] = ["P 63 m c"]
sg_fp[187,0:1] = ["P -6 m 2"] 
sg_fp[188,0:1] = ["P -6 c 2"] 
sg_fp[189,0:1] = ["P -6 2 m"] 
sg_fp[190,0:1] = ["P -6 2 c"] 
sg_fp[191,0:1] = ["P 6/m m m"]
sg_fp[192,0:1] = ["P 6/m c c"] 
sg_fp[193,0:1] = ["P 63/m c m"] 
sg_fp[194,0:1] = ["P 63/m m c"] 

#Cubic
sg_fp[195,0:1] = ["P 2 3"]
sg_fp[196,0:1] = ["F 2 3"]
sg_fp[197,0:1] = ["I 2 3"]
sg_fp[198,0:1] = ["P 21 3"]
sg_fp[199,0:1] = ["I 21 3"]
sg_fp[200,0:1] = ["P m -3"]
sg_fp[201,0:1] = ["P n -3"]
sg_fp[202,0:1] = ["F m -3"]
sg_fp[203,0:1] = ["F d -3"]
sg_fp[204,0:1] = ["I m -3"]
sg_fp[205,0:1] = ["P a -3"]
sg_fp[206,0:1] = ["I a -3"]
sg_fp[207,0:1] = ["P 4 3 2"]
sg_fp[208,0:1] = ["P 42 3 2"]
sg_fp[209,0:1] = ["F 4 3 2"]
sg_fp[210,0:1] = ["F 41 3 2"]
sg_fp[211,0:1] = ["I 4 3 2"]
sg_fp[212,0:1] = ["P 43 3 2"]
sg_fp[213,0:1] = ["P 41 3 2"]
sg_fp[214,0:1] = ["I 41 3 2"]
sg_fp[215,0:1] = ["P -4 3 m"]
sg_fp[216,0:1] = ["F -4 3 m"]
sg_fp[217,0:1] = ["I -4 3 m"]
sg_fp[218,0:1] = ["P -4 3 n"]
sg_fp[219,0:1] = ["F -4 3 c"]
sg_fp[220,0:1] = ["I -4 3 d"]
sg_fp[221,0:1] = ["P m -3 m"]
sg_fp[222,0:1] = ["P n -3 n"]
sg_fp[223,0:1] = ["P m -3 n"]
sg_fp[224,0:1] = ["P n -3 m"]
sg_fp[225,0:1] = ["F m -3 m"]
sg_fp[226,0:1] = ["F m -3 c"]
sg_fp[227,0:1] = ["F d -3 m"]
sg_fp[228,0:1] = ["F d -3 c"]
sg_fp[229,0:1] = ["I m -3 m"]
sg_fp[230,0:1] = ["I a -3 d"]

# Multiplicity of Space Group

sg_m = np.ndarray(231)

sg_m[1] = 1
sg_m[2] = 2
sg_m[3] = 2
sg_m[4] = 2
sg_m[5] = 4
sg_m[6] = 2
sg_m[7] = 2
sg_m[8] = 4
sg_m[9] = 4
sg_m[10] = 4
sg_m[11] = 4
sg_m[12] = 8
sg_m[13] = 4
sg_m[14] = 4
sg_m[15] = 8
sg_m[16] = 4
sg_m[17] = 4
sg_m[18] = 4
sg_m[19] = 4
sg_m[20] = 8
sg_m[21] = 8
sg_m[22] = 16
sg_m[23] = 8
sg_m[24] = 8
sg_m[25] = 4
sg_m[26] = 4
sg_m[27] = 4
sg_m[28] = 4
sg_m[29] = 4
sg_m[30] = 4
sg_m[31] = 4
sg_m[32] = 4
sg_m[33] = 4
sg_m[34] = 4
sg_m[35] = 8
sg_m[36] = 8
sg_m[37] = 8
sg_m[38] = 8
sg_m[39] = 8
sg_m[40] = 8
sg_m[41] = 8
sg_m[42] = 16
sg_m[43] = 16
sg_m[44] = 8
sg_m[45] = 8
sg_m[46] = 8
sg_m[47] = 8
sg_m[48] = 8
sg_m[49] = 8
sg_m[50] = 8
sg_m[51] = 8
sg_m[52] = 8
sg_m[53] = 8
sg_m[54] = 8
sg_m[55] = 8
sg_m[56] = 8
sg_m[57] = 8
sg_m[58] = 8
sg_m[59] = 8
sg_m[60] = 8
sg_m[61] = 8
sg_m[62] = 8
sg_m[63] = 16
sg_m[64] = 16
sg_m[65] = 16
sg_m[66] = 16
sg_m[67] = 16
sg_m[68] = 16
sg_m[69] = 32
sg_m[70] = 32
sg_m[71] = 16
sg_m[72] = 16
sg_m[73] = 16
sg_m[74] = 16
sg_m[75] = 4
sg_m[76] = 4
sg_m[77] = 4
sg_m[78] = 4
sg_m[79] = 8
sg_m[80] = 8
sg_m[81] = 4
sg_m[82] = 8
sg_m[83] = 8
sg_m[84] = 8
sg_m[85] = 8
sg_m[86] = 8
sg_m[87] = 16
sg_m[88] = 16
sg_m[89] = 8
sg_m[90] = 8
sg_m[91] = 8
sg_m[92] = 8
sg_m[93] = 8
sg_m[94] = 8
sg_m[95] = 8
sg_m[96] = 8
sg_m[97] = 16
sg_m[98] = 16
sg_m[99] = 8
sg_m[100] = 8
sg_m[101] = 8
sg_m[102] = 8
sg_m[103] = 8
sg_m[104] = 8
sg_m[105] = 8
sg_m[106] = 8
sg_m[107] = 16
sg_m[108] = 16
sg_m[109] = 16
sg_m[110] = 16
sg_m[111] = 8
sg_m[112] = 8
sg_m[113] = 8
sg_m[114] = 8
sg_m[115] = 8
sg_m[116] = 8
sg_m[117] = 8
sg_m[118] = 8
sg_m[119] = 16
sg_m[120] = 16
sg_m[121] = 16
sg_m[122] = 16
sg_m[123] = 16
sg_m[124] = 16
sg_m[125] = 16
sg_m[126] = 16
sg_m[127] = 16
sg_m[128] = 16
sg_m[129] = 16
sg_m[130] = 16
sg_m[131] = 16
sg_m[132] = 16
sg_m[133] = 16
sg_m[134] = 16
sg_m[135] = 16
sg_m[136] = 16
sg_m[137] = 16
sg_m[138] = 16
sg_m[139] = 32
sg_m[140] = 32
sg_m[141] = 32
sg_m[142] = 32
sg_m[143] = 3
sg_m[144] = 3
sg_m[145] = 3
sg_m[146] = 9
sg_m[147] = 6
sg_m[148] = 18
sg_m[149] = 6
sg_m[150] = 6
sg_m[151] = 6
sg_m[152] = 6
sg_m[153] = 6
sg_m[154] = 6
sg_m[155] = 6
sg_m[156] = 6
sg_m[157] = 6
sg_m[158] = 6
sg_m[159] = 6
sg_m[160] = 18
sg_m[161] = 18
sg_m[162] = 12
sg_m[163] = 12
sg_m[164] = 12
sg_m[165] = 12
sg_m[166] = 36
sg_m[167] = 36
sg_m[168] = 6
sg_m[169] = 6
sg_m[170] = 6
sg_m[171] = 6
sg_m[172] = 6
sg_m[173] = 6
sg_m[174] = 6
sg_m[175] = 12
sg_m[176] = 12
sg_m[177] = 12
sg_m[178] = 12
sg_m[179] = 12
sg_m[180] = 12
sg_m[181] = 12
sg_m[182] = 12
sg_m[183] = 12
sg_m[184] = 12
sg_m[185] = 12
sg_m[186] = 12
sg_m[187] = 12
sg_m[188] = 12
sg_m[189] = 12
sg_m[190] = 12
sg_m[191] = 24
sg_m[192] = 24
sg_m[193] = 24
sg_m[194] = 24
sg_m[195] = 12
sg_m[196] = 48
sg_m[197] = 24
sg_m[198] = 12
sg_m[199] = 24
sg_m[200] = 24
sg_m[201] = 24
sg_m[202] = 96
sg_m[203] = 96
sg_m[204] = 48
sg_m[205] = 24
sg_m[206] = 48
sg_m[207] = 24
sg_m[208] = 24
sg_m[209] = 96
sg_m[210] = 96
sg_m[211] = 48
sg_m[212] = 24
sg_m[213] = 24
sg_m[214] = 48
sg_m[215] = 14
sg_m[216] = 96
sg_m[217] = 48
sg_m[218] = 24
sg_m[219] = 96
sg_m[220] = 48
sg_m[221] = 48
sg_m[222] = 48
sg_m[223] = 48
sg_m[224] = 48
sg_m[225] = 192
sg_m[226] = 192
sg_m[227] = 192
sg_m[228] = 192
sg_m[229] = 96
sg_m[230] = 96

# Data Extractiojn from CIF files

import random

def DataExtraction(path_cif):
    start = time.time()

    for (_, _, f_dat) in os.walk(path_cif): break

    f_dat = np.array(f_dat)    
    n_data = len(f_dat)

    f_no = np.empty((n_data),dtype=object)
    for i in range(n_data):
        f_no[i] = int(f_dat[i].split(".cif")[0])

    gen_d = np.empty((n_data, 19), dtype=object)

    """
    0 ; CIF Number                       int 
    1 : Update Date                      string  
    2 : Chemical Formula Structural      string
    3 : Chemical Formula Sum             string
    4 : Structure Type                   string
    5 : Experimental Density             float
    6 ; Space Group Number               int
    7 ; Space Group Name                 string
    8 : Lattice Parameter a              float
    9 : Lattice Parameter b              float
    10 : Lattice Parameter c             float
    11 : Lattice Parameter alpha         float
    12 : Lattice Parameter beta          float
    13 : Lattice Parameter gamma         float
    14 : Unit Cell Volume                float
    15 : Unit Cell Formula, Z            int
    16 : Number of Atom                  int
    17 : Crystal System                  int
    18 : Extinction Number               int
    """
    atm_d = np.empty((n_data, 1590, 9), dtype=object)
    """
    0 : Atom Name                        string 
    1 : Atom Oxidation                   string  
    2 : Multiplicity                     int
    3 : Wyckoff Symbol                   string
    4 : position x                       float
    5 : position y                       float
    6 ; position z                       float
    7 : B_iso or Equivalent              float
    8 : Occupancy                        float
    """
    error = []

    for i in range(n_data):
        chemical_formula_structural_list=[]
        chemical_formula_sum_list=[]    

        f = open(path_cif+f_dat[i],'r',encoding='UTF8')

        while True:
            line = f.readline()
            if line == "":
                break
            if bool("_database_code_ICSD" in line):
                gen_d[i,0] = int(line.split()[1])
            if bool("_audit_update_record" in line):
                gen_d[i,1] = line.split()[1]
            elif bool("_audit_creation_date" in line):
                gen_d[i,1] = line.split()[1]            
            if bool("_chemical_formula_structural" in line):
                if bool("'" in line):
                    gen_d[i,2] = line.split("'")[1]
                elif bool(line == '_chemical_formula_structural\n'):
                    line = f.readline()
                    if bool(line == '\n'):
                        line = f.readline()
                        while True:
                            line = f.readline()
                            if bool(";" in line):
                                break
                            else:
                                chemical_formula_structural_list.append(line.split("\n")[0])
                        gen_d[i,2]=' '.join(chemical_formula_structural_list)    
                    else:
                        gen_d[i,2]=(line.split("'")[1])
                else:
                    gen_d[i,2] = line.split("\n")[0].split(' ')[1]

            if bool("_chemical_formula_sum" in line):
                if bool("'" in line):
                    gen_d[i,3] = line.split("'")[1]
                elif bool(line == '_chemical_formula_sum\n'):
                    line = f.readline()
                    if bool(line == '\n'):
                        line = f.readline()
                        while True:
                            line = f.readline()
                            if bool(";" in line):
                                break
                            else:
                                chemical_formula_sum_list.append(line.split("\n")[0])
                        gen_d[i,3]=' '.join(chemical_formula_sum_list)
                    else:
                        gen_d[i,3]=(line.split("'")[1])    
                else:
                    gen_d[i,3] = line.split("\n")[0].split(' ')[1]

            if bool("_chemical_name_structure_type" in line):
                if len(line.split()) == 1:
                    while True:
                            line = f.readline()
                            if bool("_chemical_name_mineral" in line) or bool("exptl_crystal_density_diffrn" in line):
                                break
                            gen_d[i,4] = line.split("\n")[0]
                else:
                    gen_d[i,4] = ' '.join(line.split()[1:])

            if bool("_exptl_crystal_density_diffrn" in line):
                gen_d[i,5] = float(line.split()[1])
            if bool("_space_group_IT_number" in line):
                gen_d[i,6] = int(line.split()[1])
            if bool("_space_group_name_H-M_alt" in line):
                gen_d[i,7] = line.split("'")[1]
            if bool("_cell_length_a" in line):
                if bool("(" in line):
                    gen_d[i,8] = float(line.split()[1].strip("'").split("(")[0])
                else:
                    gen_d[i,8] = float(line.split()[1].strip("'"))
            if bool("_cell_length_b" in line):
                if bool("(" in line):
                    gen_d[i,9] = float(line.split()[1].strip("'").split("(")[0])
                else:
                    gen_d[i,9] = float(line.split()[1].strip("'"))
            if bool("_cell_length_c" in line):
                if bool("(" in line):
                    gen_d[i,10] = float(line.split()[1].strip("'").split("(")[0])
                else:
                    gen_d[i,10] = float(line.split()[1].strip("'"))
            if bool("_cell_angle_alpha" in line):
                if bool("(" in line):
                    gen_d[i,11] = float(line.split()[1].strip("'").split("(")[0])
                else:
                    gen_d[i,11] = float(line.split()[1].strip("'"))
            if bool("_cell_angle_beta" in line):
                if bool("(" in line):
                    gen_d[i,12] = float(line.split()[1].strip("'").split("(")[0])
                else:
                    gen_d[i,12] = float(line.split()[1].strip("'"))          
            if bool("_cell_angle_gamma" in line):
                if bool("(" in line):
                    gen_d[i,13] = float(line.split()[1].strip("'").split("(")[0])
                else:
                    gen_d[i,13] = float(line.split()[1].strip("'"))
            if bool("_cell_volume" in line):
                gen_d[i,14] = float(line.split()[1])
            if bool("_cell_formula_units_Z" in line):
                gen_d[i,15] = int(line.split()[1])
            if bool("_atom_site_occupancy" in line):
                na = 0
                for j in range(1590):
                    line = f.readline()
                    if bool("loop_" in line) or ("#End" in line):
                        break
                    else:
                        na += 1
                        atm_d[i,j,0] = line.split()[0]
                        atm_d[i,j,1] = line.split()[1]
                        atm_d[i,j,2] = int(line.split()[2])
                        atm_d[i,j,3] = line.split()[3]

                        if line.split()[4] == "." or line.split()[4] == "-.":
                            atm_d[i,j,4] = 0.0 
                        elif bool("(" in line.split()[4]):
                            atm_d[i,j,4] = float(line.split()[4].split("(")[0])
                        else : atm_d[i,j,4] = float(line.split()[4])

                        if line.split()[5] == "." or line.split()[5] == "-.":
                            atm_d[i,j,5] = 0.0 
                        elif bool("(" in line.split()[5]):
                            atm_d[i,j,5] = float(line.split()[5].split("(")[0])
                        else : atm_d[i,j,5] = float(line.split()[5])

                        if line.split()[6] == "." or line.split()[6] == "-.":
                            atm_d[i,j,6] = 0.0                
                        elif bool("(" in line.split()[6]):
                            atm_d[i,j,6] = float(line.split()[6].split("(")[0])
                        else : atm_d[i,j,6] = float(line.split()[6])

                        if line.split()[7] == "." or line.split()[7] == "-.":
                            atm_d[i,j,7] = 0.0
                        elif bool("(" in line.split()[7]):
                            atm_d[i,j,7] = float(line.split()[7].split("(")[0])
                        else : atm_d[i,j,7] = float(line.split()[7])
                        if atm_d[i,j,7] < 0:
                            atm_d[i,j,7] = 0.0 

                        if line.split()[8] == "." or line.split()[8] == "-.":
                            atm_d[i,j,8] = 0.0
                        elif bool("(" in line.split()[8]):
                            atm_d[i,j,8] = float(line.split()[8].split("(")[0])
                        else : atm_d[i,j,8] = float(line.split()[8])                        

                gen_d[i,16] = na


        f.close()

        # Crystal System (1-7)
        if 1 <= gen_d[i,6] <= 2:
            gen_d[i,17] = 1            # Triclinic
        elif 3 <= gen_d[i,6] <= 15:
            gen_d[i,17] = 2            # Monoclinic
        elif 16 <= gen_d[i,6] <= 74:
            gen_d[i,17] = 3            # Orthorhombic
        elif 75 <= gen_d[i,6] <= 142:
            gen_d[i,17] = 4            # Tetragonal
        elif 143 <= gen_d[i,6] <= 167:
            gen_d[i,17] = 5            # Trigonal
        elif 168 <= gen_d[i,6] <= 194:
            gen_d[i,17] = 6            # Hexagonal
        elif 195 <= gen_d[i,6] <= 230:
            gen_d[i,17] = 7            # Cubic      

        # Extinction Number (1-101)
        if gen_d[i,6] in (1,2):
            gen_d[i,18] = 1            
        elif gen_d[i,6] in (3,6,10):
            gen_d[i,18] = 2            
        elif gen_d[i,6] in (4,11):
            gen_d[i,18] = 3   
        elif gen_d[i,6] in (5,8,12):
            gen_d[i,18] = 4   
        elif gen_d[i,6] in (7,13):
            gen_d[i,18] = 5           
        elif gen_d[i,6] in (9,15):
            gen_d[i,18] = 6            
        elif gen_d[i,6] == 14:
            gen_d[i,18] = 7   
        elif gen_d[i,6] in (16,25,47):
            gen_d[i,18] = 8   
        elif gen_d[i,6] == 17:
            gen_d[i,18] = 9            
        elif gen_d[i,6] == 18:
            gen_d[i,18] = 10            
        elif gen_d[i,6] == 19:
            gen_d[i,18] = 11   
        elif gen_d[i,6] == 20:
            gen_d[i,18] = 12   
        elif gen_d[i,6] in (21,35,38,65):
            gen_d[i,18] = 13            
        elif gen_d[i,6] in (22,42,69):
            gen_d[i,18] = 14            
        elif gen_d[i,6] in (23,24,44,71):
            gen_d[i,18] = 15   
        elif gen_d[i,6] in (26,28,51):
            gen_d[i,18] = 16   
        elif gen_d[i,6] in (27,49):
            gen_d[i,18] = 17            
        elif gen_d[i,6] in (29,57):
            gen_d[i,18] = 18            
        elif gen_d[i,6] in (30,53):
            gen_d[i,18] = 19            
        elif gen_d[i,6] in (31,59):
            gen_d[i,18] = 20   
        elif gen_d[i,6] in (32,55):
            gen_d[i,18] = 21   
        elif gen_d[i,6] in (33,62):
            gen_d[i,18] = 22   
        elif gen_d[i,6] in (34,58):
            gen_d[i,18] = 23            
        elif gen_d[i,6] in (36,40,63):
            gen_d[i,18] = 24            
        elif gen_d[i,6] in (37,66):
            gen_d[i,18] = 25   
        elif gen_d[i,6] in (39,67):
            gen_d[i,18] = 26   
        elif gen_d[i,6] in (41,64):
            gen_d[i,18] = 27           
        elif gen_d[i,6] == 43:
            gen_d[i,18] = 28            
        elif gen_d[i,6] in (45,72):
            gen_d[i,18] = 29            
        elif gen_d[i,6] in (46,74):
            gen_d[i,18] = 30   
        elif gen_d[i,6] == 48:
            gen_d[i,18] = 31   
        elif gen_d[i,6] == 50:
            gen_d[i,18] = 32   
        elif gen_d[i,6] == 52:
            gen_d[i,18] = 33            
        elif gen_d[i,6] == 54:
            gen_d[i,18] = 34            
        elif gen_d[i,6] == 56:
            gen_d[i,18] = 35   
        elif gen_d[i,6] == 60:
            gen_d[i,18] = 36   
        elif gen_d[i,6] == 61:
            gen_d[i,18] = 37 
        elif gen_d[i,6] == 68:
            gen_d[i,18] = 38            
        elif gen_d[i,6] == 70:
            gen_d[i,18] = 39            
        elif gen_d[i,6] == 73:
            gen_d[i,18] = 40   
        elif gen_d[i,6] in (75,81,83,89,99,111,115,123):
            gen_d[i,18] = 41         
        elif gen_d[i,6] in (76,78,91,95):
            gen_d[i,18] = 42   
        elif gen_d[i,6] in (77,84,93):
            gen_d[i,18] = 43            
        elif gen_d[i,6] in (79,82,87,97,107,119,121,139):
            gen_d[i,18] = 44            
        elif gen_d[i,6] in (80,98):
            gen_d[i,18] = 45   
        elif gen_d[i,6] in (85,129):
            gen_d[i,18] = 46   
        elif gen_d[i,6] == 86:
            gen_d[i,18] = 47 
        elif gen_d[i,6] == 88:
            gen_d[i,18] = 48            
        elif gen_d[i,6] in (90,113):
            gen_d[i,18] = 49            
        elif gen_d[i,6] in (92,96):
            gen_d[i,18] = 50   
        elif gen_d[i,6] == 94:
            gen_d[i,18] = 51         
        elif gen_d[i,6] in (100,117,127):
            gen_d[i,18] = 52   
        elif gen_d[i,6] in (101,116,132):
            gen_d[i,18] = 53            
        elif gen_d[i,6] in (102,118,136):
            gen_d[i,18] = 54            
        elif gen_d[i,6] in (103,124):
            gen_d[i,18] = 55   
        elif gen_d[i,6] in (104,128):
            gen_d[i,18] = 56   
        elif gen_d[i,6] in (105,112,131):
            gen_d[i,18] = 57 
        elif gen_d[i,6] in (106,135):
            gen_d[i,18] = 58            
        elif gen_d[i,6] in (108,120,140):
            gen_d[i,18] = 59            
        elif gen_d[i,6] in (109,122):
            gen_d[i,18] = 60   
        elif gen_d[i,6] == 110:
            gen_d[i,18] = 61   
        elif gen_d[i,6] == 114:
            gen_d[i,18] = 62   
        elif gen_d[i,6] == 125:
            gen_d[i,18] = 63            
        elif gen_d[i,6] == 126:
            gen_d[i,18] = 64            
        elif gen_d[i,6] == 130:
            gen_d[i,18] = 65   
        elif gen_d[i,6] == 133:
            gen_d[i,18] = 66   
        elif gen_d[i,6] == 134:
            gen_d[i,18] = 67 
        elif gen_d[i,6] == 137:
            gen_d[i,18] = 68            
        elif gen_d[i,6] == 138:
            gen_d[i,18] = 69            
        elif gen_d[i,6] == 141:
            gen_d[i,18] = 70           
        elif gen_d[i,6] == 142:
            gen_d[i,18] = 71          
        elif gen_d[i,6] in (143,147,149,150,156,157,162,164):
            gen_d[i,18] = 72   
        elif gen_d[i,6] in (144,145,151,152,153,154):
            gen_d[i,18] = 73            
        elif gen_d[i,6] in (146,148,155,160,166):
            gen_d[i,18] = 74            
        elif gen_d[i,6] in (158,165):
            gen_d[i,18] = 75   
        elif gen_d[i,6] in (159,163):
            gen_d[i,18] = 76   
        elif gen_d[i,6] in (161,167):
            gen_d[i,18] = 77 
        elif gen_d[i,6] in (168,174,175,177,183,187,189,191):
            gen_d[i,18] = 78            
        elif gen_d[i,6] in (169,170,178,179):
            gen_d[i,18] = 79            
        elif gen_d[i,6] in (171,172,180,181):
            gen_d[i,18] = 80     
        elif gen_d[i,6] in (173,176,182):
            gen_d[i,18] = 81          
        elif gen_d[i,6] in (184,192):
            gen_d[i,18] = 82   
        elif gen_d[i,6] in (185,188,193):
            gen_d[i,18] = 83            
        elif gen_d[i,6] in (186,190,194):
            gen_d[i,18] = 84            
        elif gen_d[i,6] in (195,200,207,215,221):
            gen_d[i,18] = 85   
        elif gen_d[i,6] in (196,202,209,216,225):
            gen_d[i,18] = 86   
        elif gen_d[i,6] in (197,199,204,211,217,229):
            gen_d[i,18] = 87 
        elif gen_d[i,6] in (198,208):
            gen_d[i,18] = 88            
        elif gen_d[i,6] in (201,224):
            gen_d[i,18] = 89            
        elif gen_d[i,6] in (203,227):
            gen_d[i,18] = 90          
        elif gen_d[i,6] == 205:
            gen_d[i,18] = 91          
        elif gen_d[i,6] == 206:
            gen_d[i,18] = 92   
        elif gen_d[i,6] == 210:
            gen_d[i,18] = 93            
        elif gen_d[i,6] in (212,213):
            gen_d[i,18] = 94            
        elif gen_d[i,6] == 214:
            gen_d[i,18] = 95   
        elif gen_d[i,6] in (218,223):
            gen_d[i,18] = 96   
        elif gen_d[i,6] in (219,226):
            gen_d[i,18] = 97 
        elif gen_d[i,6] == 220:
            gen_d[i,18] = 98            
        elif gen_d[i,6] == 222:
            gen_d[i,18] = 99            
        elif gen_d[i,6] == 228:
            gen_d[i,18] = 100  
        elif gen_d[i,6] == 230:
            gen_d[i,18] = 101


        a_rand = round(random.uniform(-0.005, 0.005), 6)
        b_rand = round(random.uniform(-0.005, 0.005), 6)
        c_rand = round(random.uniform(-0.005, 0.005), 6)
        alpha_rand = round(random.uniform(-0.005, 0.005), 6)
        beta_rand = round(random.uniform(-0.005, 0.005), 6)
        gamma_rand = round(random.uniform(-0.005, 0.005), 6)

    # triclinic
        if int(gen_d[i,6]) >= 1 and  int(gen_d[i,6]) <3 :
            gen_d[i,8] = (1+a_rand)*gen_d[i,8]
            gen_d[i,9] = (1+b_rand)*gen_d[i,9]
            gen_d[i,10] = (1+c_rand)*gen_d[i,10]
            gen_d[i,11] = (1+alpha_rand)*gen_d[i,11]
            gen_d[i,12] = (1+beta_rand)*gen_d[i,12]
            gen_d[i,13] = (1+gamma_rand)*gen_d[i,13]
    #monoclinic 
        elif int(gen_d[i,6]) >= 3 and  int(gen_d[i,6]) <16 :
            gen_d[i,8] = (1+a_rand)*gen_d[i,8]
            gen_d[i,9] = (1+b_rand)*gen_d[i,9]
            gen_d[i,10] = (1+c_rand)*gen_d[i,10]
            gen_d[i,12] = (1+beta_rand)*gen_d[i,12]

    #orthorhombic
        elif int(gen_d[i,6]) >= 16 and  int(gen_d[i,6]) <75 :
            gen_d[i,8] = (1+a_rand)*gen_d[i,8]
            gen_d[i,9] = (1+b_rand)*gen_d[i,9]
            gen_d[i,10] = (1+c_rand)*gen_d[i,10]
    #Tetragonal
        elif int(gen_d[i,6]) >=75 and int(gen_d[i,6])  < 143:
            gen_d[i,8] = (1+a_rand)*gen_d[i,8]
            gen_d[i,9] = gen_d[i,8]
            gen_d[i,10] = (1+c_rand)*gen_d[i,10]

    # Trigonal
        elif int(gen_d[i,6]) >=143 and int(gen_d[i,6])  < 168:
            gen_d[i,8] = (1+a_rand)*gen_d[i,8]
            gen_d[i,9] = gen_d[i,8]
            gen_d[i,10] = (1+c_rand)*gen_d[i,10]

    #Hexagonal
        elif int(gen_d[i,6]) >=168 and int(gen_d[i,6])  < 195:
            gen_d[i,8] = (1+a_rand)*gen_d[i,8]
            gen_d[i,9] = gen_d[i,8]
            gen_d[i,10] = (1+c_rand)*gen_d[i,10]

    #Cubic
        elif int(gen_d[i,6]) >=195 and int(gen_d[i,6])  < 231:
            gen_d[i,8] = (1+a_rand)*gen_d[i,8]
            gen_d[i,9] = gen_d[i,8]
            gen_d[i,10] = gen_d[i,8]        

    stop = time.time()
    
    return gen_d, atm_d, n_data, f_dat


# Spave Group Conversion

rd = np.pi/180.0

def SpaceGroupConversion(gen_d, atm_d, n_data):
    for i in range(n_data):
        if " Z1" in gen_d[i,7]:
            gen_d[i,7] = gen_d[i,7][0:-3]
        elif " Z" in gen_d[i,7]:
            gen_d[i,7] = gen_d[i,7][0:-2]
        elif " HR" in gen_d[i,7]:
            gen_d[i,7] = gen_d[i,7][0:-3]
        elif " H" in gen_d[i,7]:
            gen_d[i,7] = gen_d[i,7][0:-2]
        elif " R" in gen_d[i,7]:                                 # Trigonal to Hexagonal Conversion 
            gen_d[i,7] = gen_d[i,7][0:-2]
            gen_d[i,8] = 2.0 * gen_d[i,8] * np.sin(gen_d[i,11]/2.0*rd)
            gen_d[i,9] = 2.0 * gen_d[i,9] * np.sin(gen_d[i,11]/2.0*rd)
            gen_d[i,10] = gen_d[i,10] * np.sqrt(3 + 6 * np.cos(gen_d[i,11]*rd))
            gen_d[i,11] = 90.0
            gen_d[i,12] = 90.0
            gen_d[i,13] = 120.0
            gen_d[i,14] = gen_d[i,14] * 3.0
            for j in range(gen_d[i,16]):
                atm_d[i,j,4] = ( 2.0 * atm_d[i,j,4] - atm_d[i,j,5] - atm_d[i,j,6] ) / 3.0
                atm_d[i,j,5] = ( atm_d[i,j,4] + atm_d[i,j,5] - 2.0 * atm_d[i,j,6] ) / 3.0
                atm_d[i,j,6] = ( atm_d[i,j,4] + atm_d[i,j,5] + atm_d[i,j,6] ) / 3.0
        elif " S" in gen_d[i,7]:                               # Origin Shift 
            if gen_d[i,6] == 48:
                gen_d[i,7] = gen_d[i,7][0:-2]
                for j in range(gen_d[i,16]):
                    atm_d[i,j,4] = atm_d[i,j,4] + 1/4 
                    atm_d[i,j,5] = atm_d[i,j,5] + 1/4
                    atm_d[i,j,6] = atm_d[i,j,6] + 1/4
            elif gen_d[i,6] in (50,59):
                gen_d[i,7] = gen_d[i,7][0:-2]
                for j in range(gen_d[i,16]):
                    atm_d[i,j,4] = atm_d[i,j,4] + 1/4 
                    atm_d[i,j,5] = atm_d[i,j,5] + 1/4
                    atm_d[i,j,6] = atm_d[i,j,6] 
            elif gen_d[i,6] == 68:
                gen_d[i,7] = gen_d[i,7][0:-2]
                for j in range(gen_d[i,16]):
                    atm_d[i,j,4] = atm_d[i,j,4]  
                    atm_d[i,j,5] = atm_d[i,j,5] + 1/4
                    atm_d[i,j,6] = atm_d[i,j,6] + 1/4
            elif gen_d[i,6] in (70,203,227):
                gen_d[i,7] = gen_d[i,7][0:-2]
                for j in range(gen_d[i,16]):
                    atm_d[i,j,4] = atm_d[i,j,4] - 1/8
                    atm_d[i,j,5] = atm_d[i,j,5] - 1/8
                    atm_d[i,j,6] = atm_d[i,j,6] - 1/8   
            elif gen_d[i,6] in (85,129,130):
                gen_d[i,7] = gen_d[i,7][0:-2]
                for j in range(gen_d[i,16]):
                    atm_d[i,j,4] = atm_d[i,j,4] - 1/4 
                    atm_d[i,j,5] = atm_d[i,j,5] + 1/4
                    atm_d[i,j,6] = atm_d[i,j,6] 
            elif gen_d[i,6] in (86,126,201,224):
                gen_d[i,7] = gen_d[i,7][0:-2]
                for j in range(gen_d[i,16]):
                    atm_d[i,j,4] = atm_d[i,j,4] - 1/4
                    atm_d[i,j,5] = atm_d[i,j,5] - 1/4
                    atm_d[i,j,6] = atm_d[i,j,6] - 1/4  
            elif gen_d[i,6] == 88:
                gen_d[i,7] = gen_d[i,7][0:-2]
                for j in range(gen_d[i,16]):
                    atm_d[i,j,4] = atm_d[i,j,4]  
                    atm_d[i,j,5] = atm_d[i,j,5] - 1/4
                    atm_d[i,j,6] = atm_d[i,j,6] - 1/8
            elif gen_d[i,6] == 125:
                gen_d[i,7] = gen_d[i,7][0:-2]
                for j in range(gen_d[i,16]):
                    atm_d[i,j,4] = atm_d[i,j,4] - 1/4 
                    atm_d[i,j,5] = atm_d[i,j,5] - 1/4
                    atm_d[i,j,6] = atm_d[i,j,6] 
            elif gen_d[i,6] == (133,134,137,138):
                gen_d[i,7] = gen_d[i,7][0:-2]
                for j in range(gen_d[i,16]):
                    atm_d[i,j,4] = atm_d[i,j,4] - 1/4 
                    atm_d[i,j,5] = atm_d[i,j,5] + 1/4
                    atm_d[i,j,6] = atm_d[i,j,6] - 1/4  
            elif gen_d[i,6] in (141,142):
                gen_d[i,7] = gen_d[i,7][0:-2]
                for j in range(gen_d[i,16]):
                    atm_d[i,j,4] = atm_d[i,j,4] 
                    atm_d[i,j,5] = atm_d[i,j,5] + 1/4
                    atm_d[i,j,6] = atm_d[i,j,6] - 1/8  
        if gen_d[i,7] == "A e m 2":                           # Conversion to old version
            gen_d[i,7] = "A b m 2" 
        elif gen_d[i,7] == "A e a 2":
            gen_d[i,7] = "A b a 2" 
        elif gen_d[i,7] == "C m c e":
            gen_d[i,7] = "C m c a" 
        elif gen_d[i,7] == "C m m e":
            gen_d[i,7] = "C m m a"   
        elif gen_d[i,7] == "C c c e":
            gen_d[i,7] = "C c c a"
            
    return gen_d, atm_d, n_data

# General Infomation Check

def GeneralInfromCheck(gen_d, atm_d, n_data, f_dat):
    vol = np.ndarray([n_data])

    for i in range(n_data):
        if not(1 <= gen_d[i,6] <= 230):
            print("sg",gen_d[i,0],gen_d[i,6])
        if not(0.5 <= gen_d[i,8] <= 200.0):
            print("a",gen_d[i,0],gen_d[i,8])
        if not(0.5 <= gen_d[i,9] <= 200.0):
            print("b",gen_d[i,0],gen_d[i,9])
        if not(0.5 <= gen_d[i,10] <= 500.0):
            print("c",gen_d[i,0],gen_d[i,10])
        if not(5.0 <= gen_d[i,11] <= 170.0):
            print("alpha",gen_d[i,0],gen_d[i,11])
        if not(5.0 <= gen_d[i,12] <= 170.0):
            print("beta",gen_d[i,0],gen_d[i,12])
        if not(5.0 <= gen_d[i,13] <= 170.0):
            print("gamma",gen_d[i,0],gen_d[i,13])
        if not(1.0 <= gen_d[i,14] <= 500000.0):
            print("vol",gen_d[i,0],gen_d[i,14])
        if not(1.0 <= gen_d[i,15] <= 400.0):
            print("Z",gen_d[i,0],gen_d[i,15])
        if not(1.0 <= gen_d[i,16] <= 1590.0):
            print("N_atom",gen_d[i,0],gen_d[i,16])
        if not(1 <= gen_d[i,17] <= 7):
            print("cs",gen_d[i,0],gen_d[i,17])
        if not(1 <= gen_d[i,18] <= 101):
            print("en",gen_d[i,0],gen_d[i,18])

        if 1 <= gen_d[i,6] <= 2:
            vol[i] = gen_d[i,8]*gen_d[i,9]*gen_d[i,10]*np.sqrt(1-np.cos(gen_d[i,11]*rd)**2
                        -np.cos(gen_d[i,12]*rd)**2-np.cos(gen_d[i,13]*rd)**2
                        +2.0*np.cos(gen_d[i,11]*rd)*np.cos(gen_d[i,12]*rd)*np.cos(gen_d[i,13]*rd))
        if 3 <= gen_d[i,6] <= 15:
            vol[i] = gen_d[i,8]*gen_d[i,9]*gen_d[i,10]*np.sin(gen_d[i,11]*rd)\
                              *np.sin(gen_d[i,12]*rd)*np.sin(gen_d[i,13]*rd)
        if 16 <= gen_d[i,6] <= 74:
            vol[i] = gen_d[i,8]*gen_d[i,9]*gen_d[i,10]
        if 75 <= gen_d[i,6] <= 142:
            vol[i] = gen_d[i,8]*gen_d[i,9]*gen_d[i,10]
        if 143 <= gen_d[i,6] <= 167:
            if bool(" R" in gen_d[i,7]):
                vol[i] = gen_d[i,8]*gen_d[i,9]*gen_d[i,10]*np.sqrt(1-3*np.cos(gen_d[i,11]*rd)**2
                                                                    +2*np.cos(gen_d[i,11]*rd)**3)
            else:
                vol[i] = np.sqrt(3)/2*gen_d[i,8]*gen_d[i,9]*gen_d[i,10]
        if 168 <= gen_d[i,6] <= 194:
            vol[i] = np.sqrt(3)/2*gen_d[i,8]*gen_d[i,9]*gen_d[i,10]
        if 195 <= gen_d[i,6] <= 230:
            vol[i] = gen_d[i,8]*gen_d[i,9]*gen_d[i,10]
        gen_d[i,14]=vol[i]    ###cell parameter 변경으로 인한 volume 변경 반영        
        if np.abs(gen_d[i,14]-vol[i]) >= 10.0:
            print("vol {:6d} {:4d} {:4d} {} {:8.2f} {:8.2f}".format(i,gen_d[i,0],gen_d[i,6],gen_d[i,7],gen_d[i,14],vol[i]))
            print("{:12.5f} {:12.5f} {:12.5f} {:12.5f} {:12.5f} {:12.5f}".format(gen_d[i,8],gen_d[i,9],
                                                           gen_d[i,10],gen_d[i,11],gen_d[i,12],gen_d[i,13]))
    return gen_d, atm_d, n_data, f_dat

# Atomic Infomation Check
def AtomicInformCheck(gen_d, atm_d, n_data, f_dat):
    for i in range(n_data):
        for j in range(gen_d[i,16]):
            if bool("'" in atm_d[i,j,0]):
                print("A name",i,gen_d[i,0],atm_d[i,j,0])
            if bool("'" in atm_d[i,j,1]):
                print("A Oxidation",i,gen_d[i,0],atm_d[i,j,1])
            if not(1 <= atm_d[i,j,2] <= 256.0):
                print("A multiplicity",i,gen_d[i,0],atm_d[i,j,2])
            if not("A" <= atm_d[i,j,3] <= "z"):
                print("A wyckoff",i,gen_d[i,0],atm_d[i,j,3])
            if not(-5.0 <= atm_d[i,j,4] <= 5.0):
                print("A x",i,gen_d[i,0],atm_d[i,j,4])
            if not(-5.0 <= atm_d[i,j,5] <= 5.0):
                print("A y",i,gen_d[i,0],atm_d[i,j,5])
            if not(-5.0 <= atm_d[i,j,6] <= 5.0):
                print("A z",i,gen_d[i,0],atm_d[i,j,6])
            if not( 0.0 <= atm_d[i,j,7] < 200.0):
                print("A B",i,gen_d[i,0],atm_d[i,j,7])       
            if not(-1.0 <= atm_d[i,j,8] <= 100.0):
                print("A Occupancy",i,gen_d[i,0],atm_d[i,j,8])
    return gen_d, atm_d, n_data, f_dat

# Space Group Check 1
def SpaceGroupCheck1(gen_d, atm_d, n_data, f_dat):
    cc = 0
    for i in range(n_data):
        for j in range(1,231):
            if gen_d[i,6] == j:
                if gen_d[i,7] not in sg_std[j]:
                    cc += 1
                break

    # Space Group Check 2

    cc = 0
    for i in range(n_data):
        for j in range(1,231):
            if gen_d[i,6] == j:
                if gen_d[i,7] not in sg_cif[j]:
                    cc += 1
                break

    # Space Group Check 3

    cc = 0
    for i in range(n_data):
        for j in range(1,231):
            if gen_d[i,6] == j:
                if gen_d[i,7] not in sg_fp[j]:
                    cc += 1
                break

    # Space Group Check 4

    sgc = np.zeros((231, 14))

    for i in range(n_data):
        for j in range(1,231):
            if gen_d[i,6] == j:
                for k in range(14):
                    if gen_d[i,7] == sg_fp[j,k]:
                        sgc[j,k] += 1
                        break
                break

    for i in range(1,231):
        print("\n<",i,">  ",end="")
        for j in range(14):
            print("{:5.0f} ".format(sgc[i,j]),end="")
        
    return gen_d, atm_d, n_data, f_dat

# Some Rejection
def Rejection(gen_d, atm_d, n_data, f_dat):
    print("Number of entire data   :",n_data)

    n_data_e = n_data
    r_idx = np.full(n_data, True, dtype=bool )
    f_dat = np.array(f_dat)

    for i in range(n_data):
        if gen_d[i,14] > 10000:               # Volume > 10,000
            r_idx[i] = False

    gen_d = gen_d[r_idx]
    atm_d = atm_d[r_idx]
    f_dat = f_dat[r_idx]

    n_data = len(f_dat)
    print("Number of rejected data :",n_data_e - n_data)
    print("Number of selected data :",n_data)
    
    return gen_d, atm_d, n_data, f_dat