// Extract and test just the initiatives array
const fs = require('fs');

try {
    const content = fs.readFileSync('/workspace/index.html', 'utf8');
    
    // Extract the initiatives array
    const startMatch = content.match(/const initiatives = \[/);
    if (!startMatch) {
        console.log("❌ Could not find initiatives array start");
        process.exit(1);
    }
    
    const start = content.indexOf('const initiatives = [');
    const end = content.indexOf('];', start) + 2;
    
    if (end === 1) {
        console.log("❌ Could not find initiatives array end");
        process.exit(1);
    }
    
    const jsCode = content.substring(start, end);
    
    // Test if it's valid JavaScript
    eval(jsCode);
    
    console.log("✅ JavaScript syntax is valid");
    console.log(`📊 Array contains ${initiatives.length} initiatives`);
    
    // Check for any obvious issues
    let issues = [];
    initiatives.forEach((init, index) => {
        if (!init.title) issues.push(`Initiative ${index} missing title`);
        if (!init.description) issues.push(`Initiative ${index} missing description`);
        if (!init.category) issues.push(`Initiative ${index} missing category`);
        if (!init.impact) issues.push(`Initiative ${index} missing impact`);
        if (!init.beneficiaries) issues.push(`Initiative ${index} missing beneficiaries`);
        if (!init.icon) issues.push(`Initiative ${index} missing icon`);
    });
    
    if (issues.length > 0) {
        console.log("⚠️ Data issues found:");
        issues.forEach(issue => console.log("  " + issue));
    } else {
        console.log("✅ All initiatives have required fields");
    }
    
} catch (error) {
    console.log("❌ JavaScript error found:");
    console.log(error.message);
    console.log("Line:", error.stack);
}