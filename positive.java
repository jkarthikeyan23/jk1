import java.until.scanner;
public class postive_negative
{
public static void main(string[] args)
{
int n;
scanner s= new scanner (system.in);
system.out.print('enter the number you want to check:");
n=s.nextint();
if(n>0)
{
system.out.println("the given number "+n+" is postive")
}
else if(n<0)
{
system.out.println("the given number "+n+" is negative")
}
else
{
system out.println("the given number "+n+" is neither postive nor negative")
}
