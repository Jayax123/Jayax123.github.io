package app;
import java.util.ArrayList;

/**
 *  This class provides methods that perform operations on a list of generic objects.
 *  The Objects are assumed to have an appropriate implementation of the equals method.
 */
public class ArrayListServices <T> {

   /**
    * This method takes an ArrayList as a parameter and returns a new ArrayList that 
    * does not contain any duplicate data. For example, if this list was passed in: 
    * [A, B, D, A, A, E, B], the method would return a list containing: [A, B, D, E]. 
    * The ordering of the data does not matter. 
    * Assume that the parameter is not null, but it may be an empty ArrayList, in which case 
    * your method returns a new, empty ArrayList.
    * Also note that the ArrayList that is returned must be a new ArrayList which is not the 
    * same as the ArrayList passed in. In other words, the parameter must not be changed by your method code.
    */
   public ArrayList<T> deDuplicate(ArrayList<T> inputList){
      //Write your comments on how you implemented the method.
      /**
       I just made a empty array then iterated over the input array using a for loop. 
       Within that for loop I checked if each element of the 
       list was already present in the prevous loop or not if it was I would add too the new list.
      **/
      
      //TODO: Implement this method.
      ArrayList <T> no_dup = new ArrayList<T>();
      for (int index = 0; index < inputList.size(); index++) {
         if (no_dup.contains(inputList.get(index)) == false) {
         no_dup.add(inputList.get(index));
      }}
      return no_dup;
   }

   /**
    * This method takes two ArrayLists as parameters and returns a new ArrayList that 
    * contains the intersection of the data in the ArrayLists passed in. The intersection 
    * contains the elements that occur in both lists.
    * For example, if these lists were passed in: [A, B, D, A, A, E, B], [B, E, C], the method 
    * would return a list containing: [B, E]. The ordering of the data does not matter. Note that 
    * the result does not contain any duplicates.
    * Assume that the parameters are not null, but one or both may be an empty ArrayList, in which 
    * case your method returns a new, empty ArrayList.
    * Also note that the ArrayList that is returned must be a new ArrayList which is not the same as 
    * the ArrayList passed in. In other words, the parameter must not be changed by your method code.
    */
   public ArrayList<T> getSetIntersection(ArrayList<T> listA, ArrayList<T> listB){
      //Write your comments on how you implemented the method.
      /**
       I make three lists the first two are just getting rid of oissuble duplicates in the inputted two lists this
       is because running the method whithin the for loop
       would make the runtime longer then necessary. I get rid of the duplicates too make sure duplicates arnt mentioned 
       multiple times. Afterwards I just use a for loop too go over the first entered list then check if the second list contains 
       the element of the first list.
      **/
      //TODO: Implement this method.
      ArrayList <T> first_nd = new ArrayList<T>(deDuplicate(listA));
      ArrayList <T> second_nd = new ArrayList<T>(deDuplicate(listB));
      ArrayList <T> final_list = new ArrayList<T>();
      for (int index = 0; index < first_nd.size(); index++) {
         if (second_nd.contains(first_nd.get(index)) == true) {
            final_list.add(first_nd.get(index));
         }
      }
      return final_list;
   }

   /**
    *  This method takes two ArrayLists as parameters and returns a new ArrayList that 
    * contains the set difference of the data in the ArrayLists passed in. The set difference 
    * contains the elements that occur only in one or the other list, but not in both.
    * For example, if these lists were passed in: [A, B, D, A, A, E, B], [B, E, C], the method 
    * would return a list containing: [A, D, C]. The ordering of the data does not matter. Note 
    * that the result does not contain any duplicates.
    * Assume that the parameters are not null, but one or both may be an empty ArrayList. In the 
    * case where one list is empty, your method returns a new ArrayList that contains all of the 
    * elements on the other list- with no duplicates. In the case where both lists are empty, your 
    * method returns a new, empty ArrayList.
    * Also note that the ArrayList that is returned must be a new ArrayList which is not the same 
    * as the ArrayList passed in. In other words, the parameter must not be changed by your method code.
    */
   public ArrayList<T> getSetDifference(ArrayList<T> listA, ArrayList<T> listB){
      //Write your comments on how you implemented the method.
      /**
       As a good lazy programmer I did the same thing as the prevous one making three lists the first two just being the same as the two
       entered lists without the duplicates. Then I iterate the list checking for duplicates and if their is one then I just do the reverse
       and dont add to list. I then rerun the for loop a second time with the lists reversed so both lists differences are added to the ending list.
      **/
      
      //TODO: Implement this method.
      ArrayList <T> first_nd = new ArrayList<T>(deDuplicate(listA));
      ArrayList <T> second_nd = new ArrayList<T>(deDuplicate(listB));
      ArrayList <T> final_list = new ArrayList<T>();
      for (int index = 0; index < first_nd.size(); index++) {
         if (second_nd.contains(first_nd.get(index)) == false) {
            final_list.add(first_nd.get(index));
         }
      }
      for (int index = 0; index < second_nd.size(); index++) {
         if (first_nd.contains(second_nd.get(index)) == false) {
            final_list.add(second_nd.get(index));
         }
      }
      return final_list;
   }

}