#include <stdio.h>

int fn(unsigned char* mat, int i)
{
	return (mat[i/8] >> (i%8)) & 1;
}

int main()
{
	FILE* fin = fopen("data/5.txt","r");
	unsigned char mat[128] = {0};
	
	if (fin)
		{
			char ln[12];
			while (fgets(ln,12,fin))
				{
					int row = 0;
					int col = 0;
					for (int i = 0; i < 10; ++i)
						{
							char ch = ln[i];
							switch (ch)
								{
								case 'F':
									row <<= 1;
									break;
								case 'L':
									col <<= 1;
									break;
								case 'B':
									row = (row << 1) | 1;
									break;
								case 'R':
									col = (col << 1) | 1;
									break;
								default:
									fprintf(stderr,"Unexpected character: %c\n",ch);
									return 1;
								}
						}
					mat[row] |= (1 << col);
				}
			fclose(fin);
		}

	for (int i = 0; i < 1024; ++i)
		{
			int k = fn(mat,i);
			if (!k && 0 < i && i < 1023)
				{
					if (fn(mat,i+-1) & fn(mat,i+1))
						{
							printf("(%d) %d - %d - %d\n",i,fn(mat,i+5),fn(mat,i),fn(mat,i+1));
							return 0;
						}
				}
		}
	
	return 0;
}
