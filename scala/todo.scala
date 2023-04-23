case class Task(id: Int, description: String, isCompleted: Boolean)

import scala.collection.mutable.ListBuffer
import scala.io.StdIn.readLine

class ToDoList {
  private val tasks: ListBuffer[Task] = ListBuffer()

  def addTask(description: String): Unit = {
    val id = tasks.length + 1
    tasks += Task(id, description, isCompleted = false)
  }

  def completeTask(id: Int): Unit = {
    tasks.find(_.id == id) match {
      case Some(task) =>
        tasks -= task
        tasks += task.copy(isCompleted = true)
      case None => println(s"Task with id $id not found.")
    }
  }

  def deleteTask(id: Int): Unit = {
    tasks.find(_.id == id) match {
      case Some(task) => tasks -= task
      case None => println(s"Task with id $id not found.")
    }
  }

  def showTasks(): Unit = {
    tasks.foreach { task =>
      val status = if (task.isCompleted) "Completed" else "Incomplete"
      println(s"${task.id}: ${task.description} - $status")
    }
  }
}

object Main {
  def main(args: Array[String]): Unit = {
    val todoList = new ToDoList()

    while (true) {
      println("\nChoose an option:\n1. Add Task\n2. Complete Task\n3. Delete Task\n4. Show Tasks\n5. Exit")
      val option = readLine().toInt

      option match {
        case 1 =>
          println("Enter task description:")
          val description = readLine()
          todoList.addTask(description)
        case 2 =>
          println("Enter task ID to complete:")
          val id = readLine().toInt
          todoList.completeTask(id)
        case 3 =>
          println("Enter task ID to delete:")
          val id = readLine().toInt
          todoList.deleteTask(id)
        case 4 =>
          println("Current tasks:")
          todoList.showTasks()
        case 5 =>
          println("Goodbye!")
          System.exit(0)
        case _ =>
          println("Invalid option.")
      }
    }
  }
}


