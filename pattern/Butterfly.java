/**
output 

$      $
$$    $$
$$$  $$$
$$$$$$$$
$$$$$$$$
$$$  $$$
$$    $$
$      $

time O(n*m)
**/
import java.math.BigInteger;
class Butterfly{
	 public static void main(String[] args) {
	 	BigInteger  n=new BigInteger("4");

	 	//upper half
	 	for (BigInteger i=BigInteger.valueOf(1);i.compareTo(n)<=0;i=i.add(BigInteger.ONE) ) {
	 		for (BigInteger  j=BigInteger.valueOf(1);j.compareTo(i)<=0;j=j.add(BigInteger.ONE) ) {
	 			System.out.print("$");
	 		}
	 		BigInteger spaces=BigInteger.valueOf(2).multiply(n.subtract(i));
	 		for(BigInteger  k=BigInteger.valueOf(1);k.compareTo(spaces)<=0;k=k.add(BigInteger.ONE)){
	 			System.out.print(" ");
	 		}
	 		for (BigInteger  j=BigInteger.valueOf(1);j.compareTo(i)<=0;j=j.add(BigInteger.ONE) ) {
	 			System.out.print("$");
	 		}
	 		System.out.println();
	 	}


		//lower half
		for (BigInteger i=n;i.compareTo(BigInteger.ONE)>=0;i=i.subtract(BigInteger.ONE) ) {
			 		for (BigInteger  j=BigInteger.valueOf(1);j.compareTo(i)<=0;j=j.add(BigInteger.ONE) ) {
			 			System.out.print("$");
			 		}
			 		BigInteger spaces=BigInteger.valueOf(2).multiply(n.subtract(i));
			 		for(BigInteger  k=BigInteger.valueOf(1);k.compareTo(spaces)<=0;k=k.add(BigInteger.ONE)){
			 			System.out.print(" ");
			 		}
			 		for (BigInteger  j=BigInteger.valueOf(1);j.compareTo(i)<=0;j=j.add(BigInteger.ONE) ) {
			 			System.out.print("$");
			 		}
			 		System.out.println();
			 	}

	/* 	//lower half
	 	 	for (BigInteger  i=n;i.compareTo(BigInteger.ONE)>=0;/*@note"thsi is rookie mistake not to assign since it's mutable" i.subtract(BigInteger.ONE) ) {
	 		for (BigInteger  j=BigInteger.valueOf(1);j.compareTo(i)<=0;j.add(BigInteger.ONE) ) {
	 			System.out.print("$");
	 		}
	 		BigInteger spaces=BigInteger.valueOf(2).multiply(n.subtract(i));
	 		for(BigInteger  k=BigInteger.valueOf(1);k.compareTo(spaces)<=0;k.add(BigInteger.ONE)){
	 			System.out.print(" ");
	 		}
	 		for (BigInteger  j=BigInteger.valueOf(1);j.compareTo(i)<=0;j.add(BigInteger.ONE)) {
	 			System.out.print("$");
	 		}
	 		System.out.println();
	 	}*/
	}
}