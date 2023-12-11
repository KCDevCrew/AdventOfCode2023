/**
 * Code Golf: 
 * Get the correct answer to part 1, 
 * using a single line of js, 
 * with the fewest possible characters,
 * and the input filename must be a command line argument.
 */
console.log(require('fs').readFileSync(process.argv[2],'utf8').split('\n').reduce((a,l,g)=>l.slice(l.indexOf(': ')+2).split('; ').some(r=>r.trim().split(', ').some(p=>(p=p.split(' '),p[1]=='red'&&p[0]>12||p[1]=='green'&&p[0]>13||p[1]=='blue'&&p[0]>14)))?a:(a+=g+1),0))