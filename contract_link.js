


function getCurrentRecordID(executionContext) {
    // get the form context.
    var formContext = executionContext.getFormContext();

    // let's get the current record id.
    var currentRecordId = formContext.data.entity.getId();

    // current link placed here.
    var link_p1 = "https://orgfbce4f5c.crm4.dynamics.com/main.aspx?appid=fbb671b8-c310-ed11-b83d-000d3a23162d&pagetype=entityrecord&etn=cr6d0_contractmanagement&id="+currentRecordId+"";
    

    // let's set the value of cr6d0_link to the link.
    var linkField = formContext.getAttribute("new_link");
    linkField.setValue(link_p1);

    // log link_1 to the console.
    console.log(link_p1);
    return;
}