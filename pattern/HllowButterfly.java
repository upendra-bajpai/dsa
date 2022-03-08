
/**
https://www.geeksforgeeks.org/c-programs-print-interesting-patterns/
https://docs.google.com/document/d/1uh_l3ifDCfy9ljDgzK1wjaP2Vpz3sEAA4ADHAtbKfJ0/edit

* * * * *  * * * * *
* * * *      * * * *
* * *          * * *
* *              * *
*                  *
*                  *
* *              * *
* * *          * * *
* * * *      * * * *
* * * * *  * * * * *

**/
class HllowButterfly{
	public static void main(String[] args) {
		int n=5;
		for (int i=n;i>=1 ;i--) {
			for (int j=1;j<=i ;j++ ) {
				System.out.print("$");
			}

			for (int j=1;j<=2*(n-i) ;j++ ) {
				System.out.print(" ");
			}

			for (int j=1;j<=i ;j++ ) {
				System.out.print("$");
			}
			System.out.println();
		}

		//lower part
		for (int i=1;i<=n ;i++) {
			for (int j=1;j<=i ;j++ ) {
				System.out.print("$");
			}

			for (int j=1;j<=2*(n-i) ;j++ ) {
				System.out.print(" ");
			}

			for (int j=1;j<=i ;j++ ) {
				System.out.print("$");
			}
			System.out.println();
		}
	}
}