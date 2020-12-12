#include <stdio.h>
#include <string.h>

int main()
{
	FILE* fin = fopen("data/6.txt","r");
	int cnt = 0;
	if (fin)
		{
			int ans = 0;
			char ln[28];
			while (fgets(ln,27,fin))
				{
					int len = strlen(ln)-1;
					if (len < 1)
						{
							ans = 0;
							continue;
						}
					for (int i = 0; i < len; ++i)
						{
							int m = 1 << (ln[i]-'a');
							if (!(ans & m))
								{
									ans |= m;
									cnt++;
								}
						}
				}
			fclose(fin);
		}
	printf("%d\n",cnt);
	return 0;
}
