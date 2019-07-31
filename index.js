function filldata()
{

    var url=window.location.href
    var queryString = url ? url.split('?')[1] : window.location.search.slice(1);
    var obj = {};

    if (queryString)
    {
        queryString = queryString.split('#')[0];  
        var arr = queryString.split('&');
        for (var i = 0; i < arr.length; i++)
            {
                var a = arr[i].split('=');    
                var paramName = a[0];
                var paramValue = typeof (a[1]) === 'undefined' ? true : a[1];    
                paramName = paramName.toLowerCase();
                if (typeof paramValue === 'string') paramValue = paramValue.toLowerCase();      
                if (paramName.match(/\[(\d+)?\]$/))
                {
                    var key = paramName.replace(/\[(\d+)?\]/, '');
                    if (!obj[key]) obj[key] = [];      
                    if (paramName.match(/\[\d+\]$/))
                    {
                        var index = /\[(\d+)\]/.exec(paramName)[1];
                        obj[key][index] = paramValue;
                    }
                    else
                    {        
                        obj[key].push(paramValue);
                    }
               }
               else
               {        
                    if (!obj[paramName])
                    {        
                        obj[paramName] = paramValue;
                    }
                    else if (obj[paramName] && typeof obj[paramName] === 'string')
                    {          
                        obj[paramName] = [obj[paramName]];
                        obj[paramName].push(paramValue);
                    }
                    else
                    {        
                        obj[paramName].push(paramValue);
                    }
                }
            }
    }
for (var k in obj)
{
    if (obj.hasOwnProperty(k))
    {          

      if(document.getElementById(k).getAttribute("type")=='text'||document.getElementById(k).getAttribute("type")=='email')
           {
              
              document.getElementById(k).value = obj[k];
           }

           if(document.getElementById(k).getAttribute("type")!='text')
           {
              if(document.getElementById(k).tagName=="SELECT")
              { 
                  var select = document.getElementById(k);
                  for (var i = 0; i < select.length; i++)
                  {
                    var option = select.options[i].value;  
                    
                    var a=option.toLowerCase()                    
                    obj[k]=obj[k].replace("%20", " ");
                    obj[k]=obj[k].replace(/\s+/g, ' ');

                    if(obj[k] == a)
                    {
                      select.options[i].id=a;                      
                      document.getElementById(a).selected = "true"; 
                      document.getElementById(a).setAttribute("selected", "selected");
                      break;
                    }

    
                  }             
              }

           

           
            }        

       
    }

}
}