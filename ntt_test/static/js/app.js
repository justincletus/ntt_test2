function createRouter() {
    let token = $('input[name=csrfmiddlewaretoken]').val();
    let sap_id = $('input[name=sap_id]').val();
    let hostname = $('input[name=hostname]').val();
    let ip_address = $('input[name=ip_address]').val();
    let mac_address = $('input[name=mac_address]').val();
    let id = $('input[name="update_id"]').val();
    if (id) {
        $.ajax({
            headers: { "X-CSRFToken": token },
            type: 'post',
            url: '/create-router/',
            data: {
                'token': token,
                'sap_id': sap_id,
                'hostname': hostname,
                'ip_address': ip_address,
                'mac_address': mac_address,
                'id': id
            },
            dataType: 'json',
            success: function(data) {
                $('#router_details').replaceWith(
                    "<tr>" +
                    "<td>" + data.id  +"</td>" +
                    "<td>" + data.sap_id  +"</td>" +
                    "<td>" + data.hostname  +"</td>" +
                    "<td>" + data.ip_address  +"</td>" +
                    "<td>" + data.mac_address  +"</td>" +
                    "<td colspan="+"2" + ">" + 
                        "<span onclick=" + `editRouter(data.id)` +"> Edit </span> |" +
                        "<span onclick=" + `deleteRouter(data.id)` +">Delete</span>" +"</td>"
                    +"</tr>"
                )

            },
            error: function(err) {
                console.log(err)
            }
        });
    }

    if (sap_id) {
        $.ajax({
            headers: { "X-CSRFToken": token },
            type: 'post',
            url: '/create-router/',
            data: {
                'token': token,
                'sap_id': sap_id,
                'hostname': hostname,
                'ip_address': ip_address,
                'mac_address': mac_address,
                'id': id
            },
            dataType: 'json',
            success: function(data) {
                $('#router_details').append(
                    "<tr>" +
                    "<td>" +data.id  +"</td>" +
                    "<td>" +data.sap_id  +"</td>" +
                    "<td>" + data.hostname  +"</td>" +
                    "<td>" +data.ip_address  +"</td>" +
                    "<td>" + data.mac_address  +"</td>" +
                    "<td colspan="+"2" + ">" + 
                        "<span onclick=" + `editRouter(data.id)` +"> Edit </span> |" +
                        "<span onclick=" + `deleteRouter(data.id)` +">Delete</span>" +"</td>"
                    +"</tr>"
                )
                let counter_id = $('.counter_id').last().html();
                if (counter_id) {
                    window.top.location = window.top.location;
                }
                else if(counter_id == null) {
                    location.reload();
                }

            },
            error: function(err) {
                console.log(err)
            }
        })
    }
    if (!sap_id) {
        alert('Name is required');
    }
    
}



function tableDetails() {
    let tableData = []
    let x = document.getElementsByClassName('counter_id')
    for (let i=0; i < x.length; i++) {
        tableData.push(x[i].innerHTML);
    }
    
    return tableData;
}




function editRouter(id) {
    
    if (id) {
        $.ajax({
            url: '/router/' +id,
            data: {
                'id': id
            },
            dataType: 'json',
            success: function(data) {
                //console.log(data);
                $('input[name="update_id"]').val(data.id);
                $('input[name="sap_id"]').val(data.sap_id);
                $('input[name="hostname"]').val(data.hostname);
                $('input[name="ip_address"]').val(data.ip_address);
                $('input[name="mac_address"]').val(data.mac_address);
            },
            error: function(err) {
                console.log(err)
            }            
        })
        
        
    }

}

function deleteRouter(id) {
    let token = $('input[name=csrfmiddlewaretoken]').val();
    console.log(token);
    if (id) {
        $.ajax({
            headers: { "X-CSRFToken": token },
            type: 'post',
            url: '/deleteRouter/',
            data: {
                'id': id
            },
            dataType: 'json',
            success: function(data) {
                location.reload();
            },
            error: function(err) {
                console.log(err)
            }
        })
    }

    console.log(id);
}

function generateRecords() {
    let v = prompt("How number of you want create? ");
    //console.log(v);
    if (v) {
        $.ajax({
            url: '/generateRecords/',
            data: {
                'id': v
            },
            dataType: 'json',
            success: function(data) {
                $('#router_details').append(
                    "<tr>" +
                    "<td>" + data.id  +"</td>" +
                    "<td>" + data.name  +"</td>" +
                    "<td>" + data.ip_add  +"</td>" +
                    "<td colspan="+"2" + ">" + 
                        "<span onclick=" + `editRouter(data.id)` +"> Edit </span> |" +
                        "<span onclick=" + `deleteRouter(data.id)` +">Delete</span>" +"</td>"
                    +"</tr>"
                )
            },
            error: function(err) {
                console.log(err)
            }
        })

        window.top.location = window.top.location;
    }
    
}