/*
*Time Complexity= O(n)
*starts from one end and search till the last element untill the desired element is found
*/

module.exports = {
    linearSearch : linearSearch
}

function linearSearch(data,l,n,value){
    for(var i=0;i<1000000;i++){
        if(data[i]==value){
            return "find first at index "+i;
        }
    }
    return "element does not exists";   
}