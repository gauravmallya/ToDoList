import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-show-task',
  templateUrl: './show-task.component.html',
  styleUrls: ['./show-task.component.css']
})
export class ShowTaskComponent implements OnInit {

  
  constructor(private service:SharedService) { 
    
  }

  TaskList: any=[];
  ModalTitle:string;
  ActivateAddEditTask:boolean=false;
  task:any;

  ngOnInit(): void {
    this.refreshTaskList();
  }

  addClick(){
    this.task={
      TaskID:0,
      TaskName: ""
    };
    this.ModalTitle="Add a Task"
    this.ActivateAddEditTask=true;
  }

  editClick(item){
    this.task= item;
    this.ModalTitle="Edit Task";
    this.ActivateAddEditTask=true;
  }

  closeClick(){
    this.ActivateAddEditTask=false;
    this.refreshTaskList();

  }

  refreshTaskList(){
    this.service.getTasks().subscribe(data=>{
      this.TaskList=data;
    });
    console.log(this.TaskList)
  }
  
  deleteClick(TaskID){
    this.service.deleteTasks(TaskID).subscribe(res=>{
      alert(res.toString());
      this.refreshTaskList()
    });
    this.refreshTaskList()
  }


}
