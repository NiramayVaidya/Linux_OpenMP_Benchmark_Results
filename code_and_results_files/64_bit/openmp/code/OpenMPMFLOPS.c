/*
gcc OpenMPMFLOPS.c cpuidc64.o cpuida64.o -m64 -lrt -lc -lm -O3 -o notOMPmflops64
./notOMPmflops64

gcc OpenMPMFLOPS.c cpuidc64.o cpuida64.o -m64 -lrt -lc -lm -O3 -fopenmp -o openMPmflops64
./openMPmflops64

Affinity Setting
taskset 0x00000001 ./openMPmflops64


gcc OpenMPMFLOPS.c cpuidc.o cpuida.o -lrt -lc -lm -O3 -o notOMPmflops32
./notOMPmflops32

gcc OpenMPMFLOPS.c cpuidc.o cpuida.o  -lrt -lc -lm -O3 -fopenmp -o openMPmflops32
./openMPmflops32

Affinity Setting
taskset 0x00000001 ./openMPmflops32

*/

 #include <stdio.h>
 #include <stdlib.h>
 #include <ctype.h>
 #include "cpuidh.h"
 #include <malloc.h>
 #include <mm_malloc.h>

char   compiler[80] = "                Via Ubuntu 64 Bit Compiler";
char   heading[40]  = "64 Bit OpenMP MFLOPS Benchmark 1";
// char   heading[40]  = "64 Bit One CPU MFLOPS Benchmark 1";
// char   compiler[80] = "                Via Ubuntu 32 Bit Compiler";
// char   heading[40]  = "32 Bit OpenMP MFLOPS Benchmark 1";
// char   heading[40]  = "32 Bit One CPU MFLOPS Benchmark 1";

 FILE    *outfile;
 int     endit;
 int     part;
 int     opwd;

 float   *x_cpu;                  // Pointer to CPU arrays
 size_t  size_x;
 int     words     = 100000;      // E Number of words in arrays
 int     repeats   = 2500;        // R Number of repeat passes 
 int     cpu  = -1;
 float   xval = 0.999950f;
 float   aval = 0.000020f;
 float   bval = 0.999980f;
 float   cval = 0.000011f;
 float   dval = 1.000011f;
 float   eval = 0.000012f;
 float   fval = 0.999992f;
 float   gval = 0.000013f;
 float   hval = 1.000013f;
 float   jval = 0.000014f;
 float   kval = 0.999994f;
 float   lval = 0.000015f;
 float   mval = 1.000015f;
 float   oval = 0.000016f;
 float   pval = 0.999996f;
 float   qval = 0.000017f;
 float   rval = 1.000017f;
 float   sval = 0.000018f;
 float   tval = 1.000018f;
 float   uval = 0.000019f;
 float   vval = 1.000019f;
 float   wval = 0.000021f;
 float   yval = 1.000021f;

 void triadplus2(int n, float a, float b, float c, float d, float e, float f, float g, float h, float j, float k, float l, float m, float o, float p, float q, float r, float s, float t, float u, float v, float w, float y, float *x)
 {
     int i;

     #pragma omp parallel for
     for(i=0; i<n; i++)
     x[i] = (x[i]+a)*b-(x[i]+c)*d+(x[i]+e)*f-(x[i]+g)*h+(x[i]+j)*k-(x[i]+l)*m+(x[i]+o)*p-(x[i]+q)*r+(x[i]+s)*t-(x[i]+u)*v+(x[i]+w)*y;
 } 

 void triadplus(int n, float a, float b, float c, float d, float e, float f, float *x)
 {
     int i;

     #pragma omp parallel for
     for(i=0; i<n; i++)
     x[i] = (x[i]+a)*b-(x[i]+c)*d+(x[i]+e)*f;
 }

 void triad(int n, float a, float b, float *x)
 {
     int i;

     #pragma omp parallel for
     for(i=0; i<n; i++)
     x[i] = (x[i]+a)*b;
 }

 void runTests()
 {
    int  i;
    
    for (i=0; i<repeats; i++)
    {
       // calculations in CPU
       if (part == 0)
       {
          triad(words, aval, xval, x_cpu);
          opwd = 2;
       }
       if (part == 1)
       {
          triadplus(words, aval, bval, cval, dval, eval, fval, x_cpu);
          opwd = 8;
       }
       if (part == 2)
       {
          triadplus2(words, aval, bval, cval, dval, eval, fval, gval, hval, jval, kval, lval, mval, oval, pval, qval, rval, sval, tval, uval, vval, wval, yval,  x_cpu);
          opwd = 32;
       }   
 
    }
 }

 // main program that executes in the CPU
 int main(int argc, char *argv[])
 {
         
    int     i, p, g;
    int     param1;
    float   fpmops;
    float   mflops;
    char    title[3][15];
    int     isok1 = 0;
    int     isok2 = 0;
    int     count1 = 0;
    float   errors[2][10];
    int     erdata[5][10];
    float   newdata = 0.999999f;
    
    sprintf(title[0], "Data in & out ");
    for (i=1; i<7; i=i+2)
    {
       if (argc > i)
       {
          switch (toupper(argv[i][0]))
          {
               case 'W':
                param1 = 0;
                if (argc > i+1)
                {
                   sscanf(argv[i+1],"%d", &param1);
                   if (param1 > 0) words = param1;
                }
                break;

                case 'R':
                param1 = 0;
                if (argc > i+1)
                {
                   sscanf(argv[i+1],"%d", &param1);
                   if (param1 > 0) repeats = param1;
                }
                break;
 
                                case 'A':
                param1 = 0;
                if (argc > i+1)
                {
                   sscanf(argv[i+1],"%d", &param1);
                   if (param1 > -1) cpu = param1;
                }
                break;
         }
       }
    }
    int  startWords = words;
    int  startRepeats = repeats;
    local_time();
    outfile = fopen("OpenMPLog.txt","a+");
    if (outfile == NULL)
    {
        printf (" Cannot open results file \n\n");
        printf(" Press Enter\n");
        g  = getchar();
        exit (0);
    }
    getDetails();       
    printf("\n  %s %s\n\n", heading, timeday);
    for (i=0; i<10; i++)
    {
                printf("%s\n", configdata[i]);
    }
    printf("\n\n");
    fprintf (outfile, "\n"); 
    fprintf (outfile, "##############################################\n\n");
    for (i=1; i<10; i++)
    {
        fprintf(outfile, "%s \n", configdata[i]);
    }
    fprintf (outfile, "\n");
    fprintf (outfile, "##############################################\n\n");
    fprintf(outfile, "  %s %s\n", heading, timeday);
    fprintf(outfile, "  %s\n", compiler);
        if (cpu > -1) fprintf(outfile, "\n  Single CPU Affinity %d\n", cpu);
    printf("\n");
    fprintf(outfile, "\n  Test             4 Byte  Ops/   Repeat    Seconds   MFLOPS       First   All\n");
    fprintf(outfile,   "                    Words  Word   Passes                         Results  Same\n\n");
    printf("\n  Test             4 Byte  Ops/   Repeat    Seconds   MFLOPS       First   All\n");
    printf("                    Words  Word   Passes                         Results  Same\n\n");


    for (part=0; part<3; part++)
    {
          isok1  = 0;
      words = startWords;
       repeats = startRepeats;
            for (p=0; p<3; p++)
            {
               size_x = words * sizeof(float);
    
               // Allocate arrays for host CPU
               x_cpu = (float *)_mm_malloc(size_x, 16);
               if (x_cpu  == NULL)
               {
                    printf(" ERROR WILL EXIT\n");
                    printf(" Press Enter\n");
                    g  = getchar();
                    exit(1);
               }
   
               // Data for array
               for (i=0; i<words; i++)
               {
                  x_cpu[i] = newdata;
               }
               start_time();
               runTests();
               end_time();
               fpmops = (float)words * (float)opwd;
               mflops = (float)repeats * fpmops / 1000000.0f / (float)secs;
    
               // Print results
               fprintf(outfile, "%15s %9d %5d %8d %10.6f %8.0f ", title[0], words, opwd, repeats, secs, mflops);
               printf("%15s %9d %5d %8d %10.6f %8.0f ", title[0], words, opwd, repeats, secs, mflops);
                           isok1  = 0;
               float one = x_cpu[0];
               if (one == newdata)
                           {
                                   isok2 = 1;
                                   isok1 = 1;
                           }
               for (i=1; i<words; i++)
               {
                  if (one != x_cpu[i])
                  {
                     isok1 = 1;
                     if (count1 < 10)
                     {
                        errors[0][count1] = x_cpu[i];
                        errors[1][count1] = one;
                        erdata[0][count1] = i;
                                                erdata[1][count1] = words;                          
                        erdata[2][count1] = opwd;
                        erdata[3][count1] = repeats;
                        count1 = count1 + 1;
                     }
                  }
               }
               if (isok1 == 0)
               {
                  fprintf(outfile, " %10.6f   Yes\n", x_cpu[0]);
                  printf(" %10.6f   Yes\n", x_cpu[0]);
               }
               else
               {
                  fprintf(outfile, "   See later   No\n");
                  printf("   See log     No\n");
               }
                // Cleanup
               _mm_free(x_cpu);
               words = words * 10;
               repeats = repeats / 10;
               if (repeats < 1) repeats = 1; 
            }
            fprintf(outfile, "\n");
            printf("\n");
   }


    fprintf(outfile,"\n");

    if (isok2 > 0)
    {
       fprintf(outfile," ERROR - At least one first result of 0.999999 - no calculations?\n\n");
       printf(" ERROR - At least one first result of 0.999999 - no calculations?\n\n");
    }
    if (count1 > 0)
    {
       fprintf(outfile," First Unexpected Results\n");
       for (i=0; i<count1; i++)
       {
         fprintf(outfile,"%15s %9d %5d %8d word %9d was %10.6f not %10.6f\n",
           title[0], erdata[1][i], erdata[2][i], erdata[3][i], erdata[0][i], errors[0][i], errors[1][i]);
       }
       fprintf(outfile,"\n");
    }

    fclose (outfile);
    printf(" Press Enter\n");
    g  = getchar();
    return 0;
 }


