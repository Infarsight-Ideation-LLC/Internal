async function runScraper(){
 
let region=document.getElementById("region").value

let country=document.getElementById("country").value

let days=document.getElementById("days").value
 
let industryOptions=document.getElementById("industry")
 
let industries=[...industryOptions.selectedOptions].map(o=>o.value)
 
await fetch("/run_scraper",{
 
method:"POST",
 
headers:{

"Content-Type":"application/json"

},
 
body:JSON.stringify({
 
region:region,

country:country,

industry:industries,

days:days
 
})
 
})
 
loadReports()
 
}
 
 
async function loadReports(){
 
let res=await fetch("/reports")
 
let data=await res.json()
 
let table=document.getElementById("reportTable")
 
table.innerHTML=""
 
data.forEach(file=>{
 
let row=`
 
<tr>
 
<td>${file.name}</td>
<td>${file.date}</td>
<td>${file.size}</td>
 
<td>
 
<a class="action-btn" target="_blank" href="${file.view}">View</a>
 
<a class="action-btn" href="${file.download}">Download</a>
 
</td>
 
</tr>
 
`
 
table.innerHTML+=row
 
})
 
}
 
 
loadReports()
 